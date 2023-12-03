import sys
from typing import Any

import openai

from exploration_plan_generator.clients.abstact_llm_client import AbstractLLMClient

with open('pass_openai.txt') as f:
    password = f.readlines()[0]
f.close()

openai.api_key = password
requests_counter = 0
LIMIT = 4000
GPT35 = "gpt-3.5-turbo"
GPT4 = "gpt-4"

class OpenAIClient(AbstractLLMClient):

    def send_request(
        self,
        prompt: str,
        **kwargs: Any,
    ) -> str:

        global requests_counter
        if requests_counter >= LIMIT:
            sys.exit(f'total number of API requests exceeded the limit {LIMIT}')

        completion = openai.ChatCompletion.create(
            model=self.model,
            temperature=0,
            request_timeout=45,
            messages=[
                {"role": "system", "content": "You are an AI assistant for converting tasks in natural language to LDX code"},
                {"role": "user", "content": prompt}
            ]
        )
        res = completion.choices[0].message["content"]

        requests_counter += 1
        print(f"requests_counter: {requests_counter}")

        return res
