from llm_exploration_specifications.clients.abstact_llm_client import AbstractLLMClient
from llm_exploration_specifications.models.abstract_model import AbstractModel, SYSTEM_MESSAGE
from llm_exploration_specifications.prompts.out_domain.out_domain_nl2sql import out_domain_nl2sql_examples
from llm_exploration_specifications.prompts.out_domain.out_domain_sql2ldx import out_domain_sql2ldx_examples


class NL2SQL2LDX(AbstractModel):

    def __init__(self, llm_client: AbstractLLMClient):
        super().__int__(llm_client)
        self.first_prompt = nl2ldx_prompt_prefix

    def nl2ldx(self, dataset, scheme, sample, task, exclude_examples_ids, is_out_domain):
        dataset_name = dataset.split('.')[0]
        # currently supports only out-of-domain
        examples = [v for k, v in out_domain_nl2sql_examples.items() if k not in exclude_examples_ids]
        prompt = self.construct_request_multi_domains(dataset, scheme, examples, sample, task)
        sql = self.llm_client.send_request(system_message=SYSTEM_MESSAGE, prompt=self.first_prompt + "\n" + prompt)
        ldx = self.SQL2LDX(dataset_name, sql, exclude_examples_ids, is_out_domain)
        fixed_ldx = self.ldx_post_proccessing(ldx)
        return fixed_ldx

    def SQL2LDX(self, dataset_name, sql, exclude_examples_ids, is_multi_domain):
        examples = out_domain_sql2ldx_examples
        examples = [v for k, v in examples.items() if k not in exclude_examples_ids]

        exp_index = sql.lower().find("explanation")
        if exp_index != -1:
            sql = sql[:exp_index]
        sql = sql.strip('\n')

        print(f"SQL:\n{sql}")

        query = sql2ldx_prompt_prefix + ''.join(examples) + "\nNow convert the following.\nSQL:\n" + sql + "\nLDX:\n"
        ldx = self.llm_client.send_request(system_message="You are an AI assistant for converting tasks in SQL to LDX",prompt=query)
        ldx = ldx.replace(')}', ')]')
        return ldx


nl2ldx_prompt_prefix = """LDX is an extension to SQL. Instead of explicitly passing the parameters 
to the SQL built-in methods (e.g GROUP BY), it allows you use continuity variables (placeholders), which are determined during runtime.
The extension is especially useful for specifying the order of notebook's query operations and their type and parameters.
The continuity variables stores its value in order to reuse the same value in several places.

here are some basic examples how to convert tasks to LDX:

task: apply twice the same aggregation and same groupby
LDX:
    SELECT <COL>,<AGG>
    FROM table
    GROUP BY <COL>;
    
    SELECT <COL>,<AGG>
    FROM table
    GROUP BY <COL>;
    
task: apply two different aggregations, both grouped by the same column
LDX:
    SELECT <COL>,<AGG1>
    FROM table
    GROUP BY <COL>;
    
    SELECT <COL>,<AGG2>
    FROM table
    GROUP BY <COL>;
    
task: group by separately by two different columns, both aggregated with the same aggregation
LDX:
    SELECT <COL1>,<AGG>
    FROM table
    GROUP BY <COL1>;
    
    SELECT <COL2>,<AGG>
    FROM table
    GROUP BY <COL2>;
    
task: apply two completely different aggregations
LDX:
    SELECT <COL1>,<AGG1>
    FROM table
    GROUP BY <COL1>;
    
    SELECT <COL2>,<AGG2>
    FROM table
    GROUP BY <COL2>;
    
task: filter attribute ATT to some value
LDX:
    SELECT *
    FROM table
    WHERE ATT = <VALUE>;

task: make sure at some point to filter attribute ATT to some value, there might be other operations before that.
LDX:
    -- do some queries before # simulate 'at some point'
    
    SELECT *
    FROM table
    WHERE ATT = <VALUE>;
"""


sql2ldx_prompt_prefix = """LDX (Language for Data Exploration) is a specification language that extends Tregex, 
a query language for tree-structured data. It allows you to partially specify structural properties of a tree, 
as well as the nodes' labels, using continuity variables (placeholders) which are determined during runtime.
The language is especially useful for specifying the order of notebook's query operations and their type and parameters.
LDX supported operators are filter (F) and groupby with aggregation (G).

Here are examples how to convert SQL code to LDX:

do_some_operations() is omitted and translated to DESCENDANTS (rather than CHILDREN):

SQL:       
        -- do some queries before # simulate 'at some point'
        
        SELECT *
        FROM table
        WHERE 'column' = 'value';
LDX:
        BEGIN DESCENDANTS {A1}
        A1 LIKE [F,'column',eq,'value']

SQL:       
        -- do some queries before # simulate 'at some point'
        
        SELECT *
        FROM table
        WHERE <COL> = <VALUE>;
LDX:
        BEGIN DESCENDANTS {A1}
        A1 LIKE [F,<COL>,eq,<VALUE>]
        
LDX doesn't support multiple filters/aggregations/grouping in a single time, need to split it to different operations: 

SQL:       
        SELECT *
        FROM table
        WHERE 'column' = 'value1' or 'column' = 'value2';
LDX:
       BEGIN CHILDREN {A1,A2}
       A1 LIKE [F,'column',eq,'value1']
       A1 LIKE [F,'column',eq,'value2']

LDX doesn't support multiple filters/grouping/aggregations in a single time:

SQL:       
        SELECT 'column1',AVG('column2')
        FROM table
        WHERE 'column' = 'value1' or 'column' = 'value2';
        GROUP BY 'column1';
LDX:
       BEGIN CHILDREN {A1,A2}
       A1 LIKE [F,'column',eq,'value1'] and CHILDREN {B1}
        B1 LIKE [G,'column1',mean,'column2']
       A2 LIKE [F,'column',eq,'value2'] and CHILDREN {B2}
        B2 LIKE [G,'column1',mean,'column2']
        
SQL:   
        SELECT 'column1','column2',AVG('column3')
        FROM table
        GROUP BY 'column1','column2'; 
LDX:
       BEGIN CHILDREN {A1,A2}
       A1 LIKE [G,'column1',mean,'column3'] and CHILDREN {B1}
        B1 LIKE [G,'column2',mean,'column3']
"""

