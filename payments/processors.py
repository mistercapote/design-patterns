from .base import PaymentProcessor
from .methods import *

# Questão 03

class PixProcessor(PaymentProcessor):
    def create_payment(self) -> Payment:
        return PixPayment()

class CreditCardProcessor(PaymentProcessor):
    def create_payment(self) -> Payment:
        return CreditCardPayment()

class BoletoProcessor(PaymentProcessor):
    def create_payment(self) -> Payment:
        return BoletoPayment()


# Questão 8

class DebitCardProcessor(PaymentProcessor):
    def create_payment(self) -> Payment:
        return DebitCardPayment()

