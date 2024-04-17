import re
from abc import ABC
from collections import Counter


from llm_exploration_specifications.clients.abstact_llm_client import AbstractLLMClient
from nl2ldx_benchmark.evaulation.benchmark_model_api import BenchmarkModelAPI

SYSTEM_MESSAGE = "You are an AI assistant for converting tasks in natural language to LDX"

class AbstractModel(BenchmarkModelAPI, ABC):

    def __int__(self, llm_client: AbstractLLMClient):
        self.llm_client = llm_client
        self.first_prompt = ""

    def __str__(self):
        return type(self).__name__ + "-" + self.llm_client.__str__()

    def ldx_post_proccessing(self, ldx_generated):
        # post-processioning
        nodes = re.findall("<.+?>", ldx_generated)
        counts = Counter(nodes)
        for k in counts:
            if len(k) > 4:
                if counts[k] == 1:
                    ldx_generated = ldx_generated.replace(k, ".*")
                else:
                    ldx_generated = ldx_generated.replace(k, f"(?{k}.*)")
        ldx_generated = ldx_generated.replace(".*,.*,.*", ".*")
        ldx_generated = ldx_generated.replace(".*,.*", ".*")

        # remove explanation from the answer
        exp_index = ldx_generated.lower().find("explanation")
        if exp_index != -1:
            ldx_generated = ldx_generated[:exp_index]

        if ldx_generated.startswith("LDX:"):
            ldx_generated = ldx_generated[4:]

        ldx_generated = ldx_generated.replace(")}", ")]")
        return ldx_generated

    def construct_request(self, dataset_name, scheme, examples, sample, task):
        prefix = f'here are more complex examples how to convert tasks to LDX, given {dataset_name} dataset, scheme {scheme} and sample:\n {sample}:\n'
        task_section = "\nnow convert the following task to LDX according to the given scheme, and add explanation."
        request = prefix + ''.join(examples) + task_section + "\n\ntask: " + task + "\nLDX:"
        return request

    def construct_request_multi_domains(self, dataset_name, scheme, examples, sample, task):
        prefix = f'here are more complex examples how to convert tasks to LDX, given multiple domains:\n'
        task_section = f"\nnow convert the following task to LDX according to the dataset: {dataset_name} and scheme: {scheme}, and add explanation."
        sample_section = f"\nuse this sample of first 5 tuples from the dataset as a reference:\n{sample}"

        request = prefix + ''.join(examples) + task_section + sample_section + "\n\ntask: " + task + "\nLDX:"
        return request
