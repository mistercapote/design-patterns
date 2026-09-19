from channels.base import ChannelFactory, Checkout, Notification

# Questão 05 

class WebCheckout(Checkout):
    def show(self, order) -> str:
        return "Exibindo checkout Web"


class WebNotification(Notification):
    def send(self, order) -> str:
        return "Enviando notificacao Web"


class WebFactory(ChannelFactory):
    def create_checkout(self) -> Checkout:
        return WebCheckout()

    def create_notification(self) -> Notification:
        return WebNotification()