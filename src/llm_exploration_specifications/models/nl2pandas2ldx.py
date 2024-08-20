from llm_exploration_specifications.clients.abstact_llm_client import AbstractLLMClient
from llm_exploration_specifications.models.abstract_model import AbstractModel, SYSTEM_MESSAGE
from llm_exploration_specifications.prompts.in_domain.flights.flights_nl2pandas_examples import \
    flights_nl2pandas_examples
from llm_exploration_specifications.prompts.in_domain.flights.fligths_pandas2ldx_examples import \
    flights_pandas2ldx_examples
from llm_exploration_specifications.prompts.in_domain.netflix.netflix_nl2pandas_examples import netflix_nl2pandas_examples
from llm_exploration_specifications.prompts.in_domain.netflix.netflix_pandas2ldx_examples import netflix_pandas2ldx_examples
from llm_exploration_specifications.prompts.in_domain.play_store.play_store_nl2pandas_examples import play_store_nl2pandas_examples
from llm_exploration_specifications.prompts.in_domain.play_store.play_store_pandas2ldx_examples import play_store_pandas2ldx_examples
from llm_exploration_specifications.prompts.out_domain.out_domain_nl2pandas import out_domain_nl2pandas_examples
from llm_exploration_specifications.prompts.out_domain.out_domain_pandas2ldx import out_domain_pandas2ldx_examples


class NL2Pd2LDX(AbstractModel):

    def __init__(self, llm_client: AbstractLLMClient):
        super().__int__(llm_client)
        self.first_prompt = nl2pandas_prompt_prefix

    def nl2ldx(self, dataset, scheme, sample, task, exclude_examples_ids, is_out_domain):
        dataset_name = dataset.split('.')[0]
        if not is_out_domain:
            if dataset_name == "flights":
                examples = flights_nl2pandas_examples
            elif dataset_name == "netflix":
                examples = netflix_nl2pandas_examples
            elif dataset_name == "play_store":
                examples = play_store_nl2pandas_examples
            else:
                raise Exception("unsupported DB")
            examples = [v for k, v in examples.items() if int(k) not in exclude_examples_ids]
            prompt = self.construct_request(dataset, scheme, examples, sample, task)
        else:
            examples = [v for k, v in out_domain_nl2pandas_examples.items() if k not in exclude_examples_ids]
            prompt = self.construct_request_multi_domains(dataset, scheme, examples, sample, task)
        pandas = self.llm_client.send_request(system_message=SYSTEM_MESSAGE,prompt=self.first_prompt + "\n" + prompt)
        ldx = self.pandas2LDX(dataset_name, pandas, exclude_examples_ids, is_out_domain)
        fixed_ldx = self.ldx_post_proccessing(ldx)
        return fixed_ldx

    def pandas2LDX(self, dataset_name, pandas, exclude_examples_ids, is_multi_domain):
        if not is_multi_domain:
            if dataset_name == "flights":
                examples = flights_pandas2ldx_examples
            elif dataset_name == "netflix":
                examples = netflix_pandas2ldx_examples
            elif dataset_name == "play_store":
                examples = play_store_pandas2ldx_examples
            else:
                raise Exception("unsupported DB")
        else:
            examples = out_domain_pandas2ldx_examples
        examples = [v for k, v in examples.items() if k not in exclude_examples_ids]

        exp_index = pandas.lower().find("explanation")
        if exp_index != -1:
            pandas = pandas[:exp_index]
        pandas = pandas.strip('\n')

        query = pandas2ldx_prompt_prefix + ''.join(examples) + "\nNow convert the following while making sure '[' is closed by ']' and not by other parenthesis.\nPandas:\n" + pandas + "\nLDX:\n"
        ldx = self.llm_client.send_request(system_message="You are an AI assistant for converting tasks in pandas code to LDX",prompt=query)
        ldx = ldx.replace(')}', ')]')
        return ldx


nl2pandas_prompt_prefix = """LDX is an extension to python pandas. Instead of explicitly passing the parameters 
to the pandas built-in methods (e.g groupby), it allows you use continuity variables (placeholders), which are determined during runtime.
The extension is especially useful for specifying the order of notebook's query operations and their type and parameters.
The continuity variables stores its value in order to reuse the same value in several places.
LDX currently supports only the following operations: filter, groupby, agg.

here are some basic examples how to convert tasks to LDX:

task: apply twice the same aggregation and same groupby
LDX:
       agg = df.groupby(<COL>).agg(<AGG>)
       same_agg = df.groupby(<COL>).agg(<AGG>)

task: apply two different aggregations, both grouped by the same column
LDX:
        agg1 = df.groupby(<COL>).agg(<AGG1>)
        agg2 = df.groupby(<COL>).agg(<AGG2>)

task: group by separately by two different columns, both aggregated with the same aggregation
LDX:
        groupby1 = df.groupby(<COL1>).agg(<AGG>)
        groupby2 = df.groupby(<COL2>).agg(<AGG>)

task: apply two completely different aggregations
LDX:
        agg1 = df.groupby(<COL1>).agg(<AGG1>)
        agg2 = df.groupby(<COL2>).agg(<AGG2>)

task: filter attribute ATT to some value
LDX:
      some_attribute = df[df['ATT'] == <VALUE>]

task: make sure at some point to filter attribute ATT to some value, there might be other operations before that.
LDX:
      do_some_operations() # call do_some_operations() to simulate 'at some point'
      some_attribute = df[df['ATT'] == <VALUE>]
"""


pandas2ldx_prompt_prefix = """LDX (Language for Data Exploration) is a specification language that extends Tregex, 
a query language for tree-structured data. It allows you to partially specify structural properties of a tree, 
as well as the nodes' labels, using continuity variables (placeholders) which are determined during runtime.
The language is especially useful for specifying the order of notebook's query operations and their type and parameters.
LDX supported operators are filter (F) and groupby with aggregation (G).

Here are examples how to convert Pandas code to LDX:

Pandas:
       df = pd.read_csv("dataset.tsv", delimiter="\\t")
       average = df[<COL>].mean()
LDX:
        BEGIN CHILDREN {A1}
        A1 LIKE [G,.*,mean,<COL>] 


do_some_operations() is omitted and translated to DESCENDANTS (rather than CHILDREN):

Pandas:       
       df = pd.read_csv("dataset.tsv", delimiter="\\t")
       
       do_some_operations()

       some_filter = df[df['column'] == 'value']
LDX:
        BEGIN DESCENDANTS {A1}
        A1 LIKE [F,'column',eq,'value']

Pandas:       
       df = pd.read_csv("dataset.tsv", delimiter="\\t")
       
       do_some_operations()

       some_filter = df[df[<COL>] == <VALUE>]
LDX:
        BEGIN DESCENDANTS {A1}
        A1 LIKE [F,<COL>,eq,<VALUE>]
        
LDX doesn't support multiple filters/aggregations/grouping in a single time, need to split it to different operations: 

Pandas:       
       df = pd.read_csv("dataset.tsv", delimiter="\\t")

       df = df[df['column'].isin('value1','value2')]
LDX:
       BEGIN CHILDREN {A1,A2}
       A1 LIKE [F,'column',eq,'value1']
       A1 LIKE [F,'column',eq,'value2']

LDX doesn't support multiple filters/grouping/aggregations in a single time:

Pandas:       
       df = pd.read_csv("dataset.tsv", delimiter="\\t")

       df = df[df['column'].isin('value1','value2')]
       df = df.groupby('column1').agg({'column2': mean})
LDX:
       BEGIN CHILDREN {A1,A2}
       A1 LIKE [F,'column',eq,'value1'] and CHILDREN {B1}
        B1 LIKE [G,'column1',mean,'column2']
       A2 LIKE [F,'column',eq,'value2'] and CHILDREN {B2}
        B2 LIKE [G,'column1',mean,'column2']
        
Pandas:       
       df = pd.read_csv("dataset.tsv", delimiter="\\t")

       subgroups = df.groupby(['column1','column2']).agg({'column3': mean})
LDX:
       BEGIN CHILDREN {A1,A2}
       A1 LIKE [G,'column1',mean,'column3'] and CHILDREN {B1}
        B1 LIKE [G,'column2',mean,'column3']
"""

