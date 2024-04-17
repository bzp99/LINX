from llm_exploration_specifications.clients.abstact_llm_client import AbstractLLMClient
from llm_exploration_specifications.models.abstract_model import AbstractModel, SYSTEM_MESSAGE
from llm_exploration_specifications.prompts.in_domain.flights.flights_nl2ldx_examples import \
    flights_nl2ldx_examples
from llm_exploration_specifications.prompts.in_domain.netflix.netflix_nl2ldx_examples import netflix_nl2ldx_examples
from llm_exploration_specifications.prompts.in_domain.play_store.play_store_nl2ldx_examples import \
    play_store_nl2ldx_examples
from llm_exploration_specifications.prompts.out_domain.out_domain_nl2ldx import out_domain_nl2ldx_examples


class NL2LDX(AbstractModel):

    def __init__(self, llm_client: AbstractLLMClient):
        super().__int__(llm_client)
        self.first_prompt = prompt_prefix

    def nl2ldx(self, dataset, scheme, sample, task, exclude_examples_ids, is_out_domain):
        dataset_name = dataset.split('.')[0]
        if not is_out_domain:
            if dataset_name == "flights":
                examples = flights_nl2ldx_examples
            elif dataset_name == "netflix":
                examples = netflix_nl2ldx_examples
            elif dataset_name == "play_store":
                examples = play_store_nl2ldx_examples
            else:
                raise Exception("unsupported DB")
            examples = [v for k, v in examples.items() if int(k) not in exclude_examples_ids]
            prompt = self.construct_request(dataset, scheme, examples, sample, task)
        else:
            examples = [v for k, v in out_domain_nl2ldx_examples.items() if k not in exclude_examples_ids]
            prompt = self.construct_request_multi_domains(dataset, scheme, examples, sample, task)
        ldx = self.llm_client.send_request(system_message=SYSTEM_MESSAGE ,prompt=self.first_prompt + "\n" + prompt)
        fixed_ldx = self.ldx_post_proccessing(ldx)
        return fixed_ldx


prompt_prefix = """LDX (Language for Data Exploration) is a specification language that extends Tregex, 
a query language for tree-structured data. It allows you to partially specify structural properties of a tree, 
as well as the nodes' labels. The language is especially useful for specifying the order of notebook's query 
operations and their type and parameters.

here are some basic examples how to convert tasks to LDX:

task: apply twice the same aggregation and same groupby
LDX:
      BEGIN CHILDREN {A1,A2}
      A1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
      A2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]

task: apply two different aggregations, both grouped by the same column
LDX:
      BEGIN CHILDREN {A1,A2}
      A1 LIKE [G,<COL>,<AGG_FUNC1>,<AGG_COL1>]
      A2 LIKE [G,<COL>,<AGG_FUNC2>,<AGG_COL2>]

task: group by separately by two different columns, both aggregated with the same aggregation
LDX:
      BEGIN CHILDREN {A1,A2}
      A1 LIKE [G,<COL1>,<AGG_FUNC>,<AGG_COL>]
      A2 LIKE [G,<COL2>,<AGG_FUNC>,<AGG_COL>]

task: apply two completely different aggregations
LDX:
      BEGIN CHILDREN {A1,A2}
      A1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
      A2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]

task: filter attribute ATT to some value
LDX:
      BEGIN CHILDREN {A1}
      A1 LIKE [F,ATT,eq,<VALUE>]

task: make sure at some point to filter attribute ATT to some value, there might be other operations before that.
LDX:
      BEGIN DESCENDANTS {A1}
      A1 LIKE [F,ATT,eq,<VALUE>]
"""

