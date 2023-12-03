import re
import time
from abc import ABC, abstractmethod
from collections import Counter

from openai.error import RateLimitError

from exploration_plan_generator.clients.abstact_llm_client import AbstractLLMClient


class AbstractTranslationModel(ABC):

    def __int__(self, llm_client: AbstractLLMClient):
        self.llm_client = llm_client
        self.first_prompt = ""

    def __str__(self):
        return type(self).__name__ + "-" + self.llm_client.model

    @abstractmethod
    def nl2ldx(self, dataset_name, scheme, sample, task, excludes_examples_ids, is_multi_domain):
        pass

    def nl2ldx_wrapper(self, dataset, scheme, sample, task, exclude_examples_ids=[], is_out_domain=True):
        try:
            return self.nl2ldx(dataset, scheme, sample, task, exclude_examples_ids, is_out_domain)
        except RateLimitError as rle:
            sleep = 50
            print(rle)
            print(f"waiting {sleep} seconds.")
            time.sleep(sleep)
            return self.nl2ldx(dataset, scheme, sample, task, exclude_examples_ids, is_out_domain)

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

        # TODO change <A1,A2> to {A1,A2} in all pandas2ldx examples, then code here conversion '{' -> '>' before exiting
        # ldx_generated = ldx_generated.replace("{", "<").replace("}", ">")

        # remove explanation from the answer
        exp_index = ldx_generated.lower().find("explanation")
        if exp_index != -1:
            ldx_generated = ldx_generated[:exp_index]

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
