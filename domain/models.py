# Questão 03

class Order:
    def __init__(self, amount: float):
        self._amount = amount
        self.payment_method = None

    def total(self) -> float:
        return self._amount

