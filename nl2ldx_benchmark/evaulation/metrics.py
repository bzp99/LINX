import json
import re
from typing import Any

import Levenshtein
import zss
from zss import simple_distance, Node

from nl2ldx_benchmark.evaulation.xted_utils import zss_representation, ZssNode, zss_label_distance


class Metrics:
    def __init__(self):
        self.count = 0
        self.nodes_score = 0
        self.nodes_cross_score = 0
        self.structure_score = 0
        self.structure_score_zss = 0
        self.action_dist = 0

    def __str__(self):
        return f"""count: {self.count},
        structure_levinshtein_score: {self.structure_score},
        structure_zss_score: {self.structure_score_zss},
        nodes_jaccard_score: {self.nodes_score},
        nodes_cross_levinshtein_score: {self.nodes_cross_score},
        action_dist: {self.action_dist}\n"""

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


# region Structure distance

def normalized_zss_action_distance(ldx1: str, ldx2: str) -> (int, Any):
    try:
        tree1 = zss_representation(ldx1)
        tree2 = zss_representation(ldx2)

        mask1, mask2 = get_ldx_tree_mask(tree1), get_ldx_tree_mask(tree2)
        mask_ldx_tree(tree1, mask1)
        mask_ldx_tree(tree2, mask2)

        max_size = max(tree1.get_tree_size(), tree2.get_tree_size())
        distance = zss.simple_distance(tree1, tree2, ZssNode.get_children, ZssNode.get_label,
                                       label_dist=zss_label_distance)
        normalized_distance = 1 - distance / (max_size - 1)
        return normalized_distance, None
    except Exception as e:
        return 0, e


def mask_ldx_tree(node: ZssNode, mask: dict):
    Q = [node]

    while len(Q):
        curr = Q.pop(0)
        action = curr.label

        if action.action_type == "filter":
            cv1, cv2, cv3 = extract_cv(action.action_params['field']), extract_cv(
                action.action_params['condition']), extract_cv(action.action_params['term'])
            if cv1:
                action.action_params['field'] = action.action_params['field'].replace(cv1, mask.get(cv1))
            if cv2:
                action.action_params['condition'] = action.action_params['condition'].replace(cv2, mask.get(cv2))
            if cv3:
                action.action_params['term'] = action.action_params['term'].replace(cv3, mask.get(cv3))
        if action.action_type == "group":
            cv1, cv2, cv3 = extract_cv(action.action_params['field']), extract_cv(
                action.action_params['aggregations'][0]['field']), extract_cv(
                action.action_params['aggregations'][0]['type'])
            if cv1:
                action.action_params['field'] = action.action_params['field'].replace(cv1, mask.get(cv1))
            if cv2:
                action.action_params['aggregations'][0]['field'] = action.action_params['aggregations'][0][
                    'field'].replace(cv2, mask.get(cv2))
            if cv3:
                action.action_params['aggregations'][0]['type'] = action.action_params['aggregations'][0][
                    'type'].replace(cv3, mask.get(cv3))

        for child in curr.get_children(curr):
            Q.append(child)


def get_ldx_tree_mask(tree: ZssNode):
    f_args_counter, g_args_counter = [0, 0, 0], [0, 0, 0]
    f_args_naming, g_args_naming = ["field", "condition", "term"], ["field", "agg_func", "agg_field"]
    masks = {}
    Q = [tree]

    while len(Q):
        curr = Q.pop(0)
        action = curr.label
        candidates = []
        args_counter, args_naming = None, None

        if action.action_type == "filter":
            operator, field, condition, term = action.action_type, action.action_params['field'], action.action_params[
                'condition'], action.action_params['term']
            candidates = [field, condition, term]
            args_counter, args_naming = f_args_counter, f_args_naming
        if action.action_type == "group":
            operator, field, agg_func, agg_field = action.action_type, action.action_params['field'], \
            action.action_params['aggregations'][0]['type'], action.action_params['aggregations'][0]['field']
            candidates = [field, agg_func, agg_field]
            args_counter, args_naming = g_args_counter, g_args_naming

        for i, candidate in enumerate(candidates):
            cv = extract_cv(candidate)
            if not cv: continue
            if cv not in masks:
                args_counter[i] += 1
                masks[cv] = f"{operator}-{args_naming[i]}-{args_counter[i]}"

        for child in curr.get_children(curr):
            Q.append(child)

    return masks


def extract_cv(param):
    cvs = re.findall("\<.+?\>", param)
    if len(cvs) != 1:
        return None
    return cvs[0][1:-1]  # remove parenthesis


#  ZSS Score
def zss_distance(ldx_label, ldx_model_output):
    try:
        ldx_model_output = ldx_model_output.lower()
        ldx_label = ldx_label.lower()

        tree1, size1 = build_tree(ldx_model_output)
        tree2, size2 = build_tree(ldx_label)

        distance = simple_distance(tree1, tree2)
        max_size = max(size1, size2)
        result = 1 - distance / (max_size - 1)  # TODO -1 for the BEGIN node which we don't count ?
        return result
    except Exception as e:
        print(e)
        return 0


def build_tree(query):
    line_number = [0]
    query = re.sub('[<>{}]', '', query)
    lines = query.split("\n")
    return build_tree_rec(lines, line_number), len(lines)


def build_tree_rec(lines, line_number):
    line = lines[line_number[0]].lower()
    node = Node("node")  # no importance for the label
    if "children" in line or "descendants" in line:  # TODO handle also descendants
        keyword = "children" if "children" in line else "descendants"
        children = line[line.find(keyword) + 9:].split(",")
        for child_name in children:
            line_number[0] += 1
            if child_name == "*":
                continue  # node.addkid(Node("*"))
            elif line_number[0] <= len(lines) - 1:  # avoiding OOI if the output is bad
                node.addkid(build_tree_rec(lines, line_number))
    return node


#  Basic Levenshtein score
def structure_distance_metric(ldx_label, ldx_model_output):
    ldx_model_output = ldx_model_output.lower()
    ldx_label = ldx_label.lower()

    pair = (ldx_model_output, ldx_label)
    converted_pair = []
    for ldx in pair:
        ldx = ldx.replace("\n", "").replace("   ", "")
        ldx = re.sub("\[f.+?\]", "[f]", ldx)
        ldx = re.sub("\[g.+?\]", "[g]", ldx)
        converted_pair.append(ldx)
    return 1 - Levenshtein.distance(converted_pair[0], converted_pair[1]) / max(len(converted_pair[0]),
                                                                                len(converted_pair[1]))


# endregion

# region Nodes Score

# Jaccard similarity
def nodes_distance_metric(ldx_label, ldx_model_output):
    ldx_model_output = ldx_model_output.lower()
    ldx_label = ldx_label.lower()

    pair = (ldx_model_output, ldx_label)
    nodes_pair = []
    for ldx in pair:
        nodes = re.findall("\[.+?\]", ldx)
        nodes_pair.append(set(nodes))
    return len(nodes_pair[0].intersection(nodes_pair[1])) / len(nodes_pair[0].union(nodes_pair[1]))


# Best cross Levenshtein distance
def nodes_cross_distance_metric(ldx_label, ldx_model_output):
    ldx_model_output = ldx_model_output.lower()
    ldx_label = ldx_label.lower()

    ldx_model_output_nodes = set(re.findall("\[.+?\]", ldx_model_output))
    ldx_label_nodes = set(re.findall("\[.+?\]", ldx_label))
    score = 0
    for a in ldx_label_nodes:
        best = float('-inf')
        for b in ldx_model_output_nodes:
            best = max(best, 1 - Levenshtein.distance(a, b) / max(len(a), len(b)))
        score += best

    return max(0, score / len(ldx_label_nodes))


# Simple number of nodes comparison
def nodes_number_metric(ldx_label, ldx_model_output):
    ldx_model_output = ldx_model_output.lower()
    ldx_label = ldx_label.lower()

    ldx_model_output_nodes = list(re.findall("\[.+?\]", ldx_model_output))
    ldx_label_nodes = list(re.findall("\[.+?\]", ldx_label))
    return 1 - abs(len(ldx_model_output_nodes) - len(ldx_label_nodes)) / max(len(ldx_model_output_nodes),
                                                                             len(ldx_label_nodes))
# endregion
