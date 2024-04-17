from abc import abstractmethod, ABC
from typing import Any


class AbstractLLMClient(ABC):

    @abstractmethod
    def send_request(self,
                     system_message: str,
                     prompt: str,
                     **kwargs: Any) -> str:
        pass
