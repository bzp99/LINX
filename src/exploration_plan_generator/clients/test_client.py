from typing import Any

from exploration_plan_generator.clients.abstact_llm_client import AbstractLLMClient


class TestClient(AbstractLLMClient):

    def __init__(self, model):
        self.model = model
        # self.client = OpenAI()

    def __str__(self):
        return self.model

    def send_request(
            self,
            system_message: str,
            prompt: str,
            **kwargs: Any,
    ) -> str:
        return "Test"
