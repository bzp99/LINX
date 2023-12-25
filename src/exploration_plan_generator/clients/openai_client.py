from typing import Any

from openai import OpenAI

from exploration_plan_generator.clients.abstact_llm_client import AbstractLLMClient
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)

with open('pass_openai.txt') as f:
    password = f.readlines()[0]
f.close()

requests_counter = 0
GPT35 = "gpt-3.5-turbo"
GPT4 = "gpt-4"

class OpenAIClient(AbstractLLMClient):

    def __init__(self, model):
        self.model = model
        self.client = OpenAI(api_key=password)

    def __str__(self):
        return self.model

    @retry(wait=wait_random_exponential(min=1, max=30), stop=stop_after_attempt(3))
    def send_request(
            self,
            system_message: str,
            prompt: str,
            **kwargs: Any,
        ) -> str:
        chat_completion = self.client.chat.completions.create(
            model=self.model,
            temperature=0,
            timeout=45,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
        )

        res = chat_completion.choices[0].message.content

        return res
