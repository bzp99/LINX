from abc import ABC, abstractmethod


class BenchmarkModelAPI(ABC):

    @abstractmethod
    def nl2ldx(self, dataset_name, scheme, sample, task, excludes_examples_ids, is_multi_domain):
        pass
