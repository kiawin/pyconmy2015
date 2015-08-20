
class Calculator:
    """
    Simple calculator class
    """

    def __init__(self):
        pass

    def add(self, no1, no2):
        return no1+no2

    def sub(self, no1, no2):
        return no1-no2

    def mul(self, no1, no2):
        return no1*no2

    def div(self, no1, no2):
        if no2 == 0:
            # raise something else than ZeroDivisionError
            raise Exception("Haha Very Funny")
        return no1/no2
