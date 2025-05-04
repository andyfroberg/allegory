from abc import ABCMeta, abstractmethod

class View(metaclass=ABCMeta):
    @abstractmethod
    def update(self, **kwargs):
        pass

    @abstractmethod
    def draw(self, **kwargs):
        pass
