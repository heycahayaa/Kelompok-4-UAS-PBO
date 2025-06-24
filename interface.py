class Baking(ABC):
    @abstractmethod
    def bake(self): pass

class Packaging(ABC):
    @abstractmethod
    def pack(self): pass

class Labeling(ABC):
    @abstractmethod
    def label(self): pass
