from .base import Payment

# Questão 03

class PixPayment(Payment):
    def pay(self, amount: float) -> str:
        return "PIX"

class CreditCardPayment(Payment):
    def pay(self, amount: float) -> str:
        return "CREDIT_CARD"

class BoletoPayment(Payment):
    def pay(self, amount: float) -> str:
        return "BOLETO"

