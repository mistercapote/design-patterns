from abc import ABC, abstractmethod

# Questao 04

class Checkout(ABC):
    @abstractmethod
    def show(self, order) -> str:
        """Exibe o checkout específico do canal."""
        pass


class Notification(ABC):
    @abstractmethod
    def send(self, order) -> str:
        """Envia a notificação específica do canal."""
        pass


class ChannelFactory(ABC):
    @abstractmethod
    def create_checkout(self) -> Checkout:
        pass

    @abstractmethod
    def create_notification(self) -> Notification:
        pass