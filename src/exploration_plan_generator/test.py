import pandas as pd

from exploration_plan_generator.clients.openai_client import *
from exploration_plan_generator.models.nl2pandas2ldx import NL2Pd2LDX

df = pd.read_csv('..\..\datasets\play_store.tsv', sep='\t', header=0)


model = NL2Pd2LDX(OpenAIClient(model=GPT4))
dataset = 'play_store.tsv'
scheme = list(df.columns)[1:]
sample = df.head().to_string(index=False, justify='left')
task = 'Display the maximum price among two distinct subsets of applications.'

ldx = model.nl2ldx_wrapper(dataset, scheme, sample, task)
print(ldx)
