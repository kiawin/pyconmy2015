
from calculator import Calculator
import yaml

class Accounting:

    def __init__(self):
        self.data = self._load("instructions.yaml")
        self.c = Calculator()

    def _load(self, filename):
        with open(filename) as f:
            data = yaml.load(f)
        return data

    def _loop(self, method, numbers):
        result = None
        for number in numbers:
            result = number if result is None else getattr(self.c, method)(result, number)
        return result

    def add(self, *numbers):
        return self._loop("add", numbers)

    def sub(self, *numbers):
        return self._loop("sub", numbers)

    def mul(self, *numbers):
        return self._loop("mul", numbers)

    def div(self, *numbers):
        return self._loop("div", numbers)

    def process(self, name):
        result = self.data[name].pop(0)["initial"]

        for instruction in self.data[name]:
            for operation, numbers in instruction.items():
                numbers = [result]+numbers if type(numbers) == list else [result, numbers]
                result = getattr(self, operation)(*numbers)

        return result


