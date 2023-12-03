from abc import abstractmethod, ABC
from typing import Any


class AbstractLLMClient(ABC):

    def __init__(self, model):
        self.model = model

    @abstractmethod
    def send_request(self,
                     prompt: str,
                     **kwargs: Any) -> str:
        pass
