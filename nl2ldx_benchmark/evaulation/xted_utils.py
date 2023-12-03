import re

import ujson
from math import floor


class ZssNode(object):
    def __init__(self, label):
        self.label = label
        self.my_children = list()

    @staticmethod
    def get_children(node):
        return node.my_children

    def get_label(node):
        return node.label

    def add_kid(self, node, before=False):
        if before:
            self.my_children.insert(0, node)
        else:
            self.my_children.append(node)
        return self

    def add_father(self, node):
        node.my_children.append(self)

    def get_tree_size(self):
        size = 1
        children = self.get_children(self)
        if children:
            size = size + sum(child.get_tree_size() for child in children)
        return size


class Action:
    """
    Represents an analysis action within a session.
    """
    # child_display = relationship('Display', backref='parent_action', lazy='joined')

    # SUPPORTED ACTIONS
    BACK = 'back'
    SORT = 'sort'
    FILTER = 'filter'
    GROUP = 'group'
    PROJECT = 'project'

    # AGGREGATE = 'aggregate'

    def __init__(self):
        self.DATE_FORMAT = None
        self.creation_time = None
        self.child_display = None
        self.parent_display = None
        self.action_params = None
        self.action_type = None
        self.children_type = None
        self.session_id = None
        self.action_number = None
        self.action_id = None

    def __repr__(self):
        return '<Action(Type="{}")>'.format(
            self.action_type)

    def to_dict(self):
        return {
            'action_id': self.action_id,
            'action_number': self.action_number,
            'action_type': self.action_type,
            'chidren_type': self.children_type,
            'action_params': self.action_params,
            'parent_display': self.parent_display.display_id if self.parent_display else "",
            'child_display': self.child_display.display_id if self.child_display else "",
            'creation_time': self.creation_time.strftime(self.DATE_FORMAT) if self.creation_time else ""
        }

    def from_dict(self, action_dict):
        self.action_type = action_dict["action_type"]
        self.action_params = action_dict["action_params"]

    def eq(self, another_action):
        if self.action_type == another_action.action_type:
            if ujson.dumps(self.action_params) == ujson.dumps(another_action.action_params):
                return True
        return False


def zss_label_distance(action1, action2, verbose=False):
    """
    Return the edit distance of 2 labels of zss nodes
    uses action similarity for action type node,
    and display similarity for display nodes.

    :param unit:
    :param action1,action2: labels fetched with get_label
    :param verbose: If True, details will be printed.
    :return: a distance from range [0,1]
    """
    # global similarity_method

    if action1 == '' or action2 == '':
        # if verbose:
        # print("\nOne of them is None, return 10000")
        return 0.5  # TODO why 0.5 and not 0?

    if verbose:
        print(action_similarity(action1, action2), floor((1 - action_similarity(action1, action2))))
    return 1 - action_similarity(action1, action2)


def zss_representation(query):
    line_number = [0]
    # query = re.sub('[<>{}]', '', query)
    lines = query.split("\n")
    tree = zss_representation_rec(lines, line_number)
    tree_size = tree.get_tree_size()

    if tree_size != len(lines):
        raise Exception(f"tree size doesn't match: {tree_size=},{len(lines)=},{query=}")

    return tree


def zss_representation_rec(lines, line_number):
    line = lines[line_number[0]].lower()
    actions = re.findall("\[.+?\]", line)

    action = Action()
    if len(actions) > 1:
        raise Exception(f"only one action expected, got: {len(actions)}, ldx: {lines}")
    elif len(actions) == 0:
        action.action_type = 'begin'
    else:
        args = actions[0].replace('[', '').replace(']', '').split(',')
        while len(args) < 4:
            args.append('.*')
        if len(args) > 4:
            args = args[:3] + [','.join(args[3:])]
            # raise Exception(f"too much args to create action: {args}")
        operation, arg1, arg2, arg3 = args
        if operation == "f":
            action.from_dict(
                {"action_type": 'filter', "action_params": {"field": arg1, "condition": arg2, "term": arg3}})
        elif operation == "g":
            action.from_dict({"action_type": 'group',
                              "action_params": {"field": arg1, "aggregations": [{"field": arg3, "type": arg2}]}})
        else:
            raise Exception(f"invalid operation type {operation}, ldx: {lines}")

    node = ZssNode(action)

    if "children" in line or "descendants" in line:  # TODO handle also descendants
        keyword = "children" if "children" in line else "descendants"
        action.children_type = keyword
        children = line[line.find(keyword) + 9:].split(",")
        for child_name in children:
            line_number[0] += 1
            if child_name == "*":
                continue  # action.addkid(Node("*"))
            elif line_number[0] <= len(lines) - 1:  # avoiding OOI if the output is bad
                node.add_kid(zss_representation_rec(lines, line_number))
    return node


def get_aggregation_template(aggregation1, aggregation2, verbose=False):
    """
    Compute the list action template , i.e. common attributes.
    Currently should use only in "aggregation" comparison.

    :param action1, action2: Two actions
    :param verbose: If True, details will be printed.
    :return: an action template
    """
    """
    df1 = Dataframe(action_list1)
    df2 = Dataframe(action_list1)
    identicals = df1.merge(df2, how='inner').values
    fields= df1.merge(df2,how='inner' on 'field')
"""
    aggregation_template = []
    dict1 = {item['field']: item['type'] for item in aggregation1}
    dict2 = {item['field']: item['type'] for item in aggregation2}

    fields1 = set(dict1.keys())
    fields2 = set(dict2.keys())
    mutual_fields = fields1.intersection(fields2)

    for field in mutual_fields:
        if dict1[field] == dict2[field]:
            aggregation_template.append({"field": field, "type": dict1[field]})
            dict1.pop(field)
            dict2.pop(field)
        else:
            aggregation_template.append({"field": field, "type": None})

    types1 = set(dict1.values())
    types2 = set(dict2.values())
    mutual_types = types1.intersection(types2)
    for agg_type in mutual_types:
        aggregation_template.append({"field": None, "type": agg_type})

    return aggregation_template


def get_action_template(action1, action2, ignore_agg=False, verbose=False):
    """
    Compute the action template , i.e. common attributes.

    :param action1, action2: Two actions
    :param verbose: If True, details will be printed.
    :return: an action template
    """
    if action1.action_type != action2.action_type:
        return None

    template = Action()
    template.action_type = action1.action_type
    template_params = {}
    action1 = action1.action_params
    action2 = action2.action_params
    for key in action1.keys():
        if key == 'groupPriority':
            continue

        # hack for dirty data:
        if action1[key] == "~!~" or action2[key] == "~!~":
            template_params[key] = None
        elif action1[key] == action2[key]:
            template_params[key] = action1[key]
        elif key == "aggregations":
            if ignore_agg:
                template_params[key] = []
            else:
                template_params[key] = get_aggregation_template(action1[key], action2[key])

        elif type(action1[key]) == dict:
            template_params[key] = get_action_template(action1[key], action2[key])
        else:
            # print(action1[key],action2[key])
            template_params[key] = None
    template.action_params = template_params
    if verbose:
        print(template.to_dict())
    return template


def action_similarity(action1: Action, action2: Action, verbose=False):
    """
    Compute the similarity between a 2 actions dictionaries.

    :param action1:
    :param action1, action2: Two actions
    :param verbose: If True, details will be printed.
    :return: a similarity rank ranging [0,1] where 1 means identity. 
    """
    if verbose:
        print("Action similarity for:", action1.action_id,
              "(", action1.action_type, ",", action1.action_params, ")",
              ",", action2.action_id,
              "(", action2.action_type, ",", action2.action_params, ")",
              )

    if action1.action_type != action2.action_type:
        if verbose:
            print("\trank:0 (different types)")
        return 0.0

    if action1.action_type == "begin":
        return 1

    t = get_action_template(action1, action2).action_params
    if verbose:
        print("\tGenerating template:", t)
    none_count = 0.0
    match_count = 0.0

    for key in t.keys():
        if type(t[key]) == list:
            if not t[key] and (action1.action_params[key] or action2.action_params[key]):
                none_count += 0.3
                continue
            for sub_dict in t[key]:
                for v in sub_dict.values():
                    if v is None:
                        none_count += 0.3
                    else:
                        match_count += 1

        if t[key] is None:
            none_count += 1
        else:
            match_count += 1
    abs_rank = match_count / (match_count + none_count)
    if verbose:
        print("\trank:", abs_rank, ". match count:", match_count, ",none count:", none_count)

    score = 0.5 + abs_rank / 2  # starting from 0.5 since the operation type is the same
    if action1.children_type != action2.children_type:
        score /= 2
    return score


__all__ = ['action_similarity']
