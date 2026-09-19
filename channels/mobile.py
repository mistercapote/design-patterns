from channels.base import ChannelFactory, Checkout, Notification

# Questão 05 

class MobileCheckout(Checkout):
    def show(self, order) -> str:
        return "Exibindo checkout Mobile"


class MobileNotification(Notification):
    def send(self, order) -> str:
        return "Enviando notificacao Mobile"


class MobileFactory(ChannelFactory):
    def create_checkout(self) -> Checkout:
        return MobileCheckout()

    def create_notification(self) -> Notification:
        return MobileNotification()