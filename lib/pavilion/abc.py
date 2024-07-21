from abc import ABC, abstractmethod

class Cancellable(ABC):
    @abstractmethod
    def cancel(self, *args, **kwargs) -> None:
        ...
