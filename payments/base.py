from abc import ABC, abstractmethod

# Questão 03

class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        """Executa o pagamento e devolve o identificador/resultado."""
        pass


class PaymentProcessor(ABC):
    @abstractmethod
    def create_payment(self) -> Payment:
        """Factory Method que deve ser implementado pelas subclasses."""
        pass

    def process_order(self, order) -> str:
        """Fluxo comum que delega a criação do pagamento ao Factory Method."""
        payment = self.create_payment()
        method_used = payment.pay(order.total())
        order.payment_method = method_used
        return method_used
