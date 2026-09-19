from channels.base import ChannelFactory, Checkout, Notification

# Questão 05

class KioskCheckout(Checkout):
    def show(self, order) -> str:
        return "Exibindo checkout Kiosk"


class KioskNotification(Notification):
    def send(self, order) -> str:
        return "Enviando notificacao Kiosk"


class KioskFactory(ChannelFactory):
    def create_checkout(self) -> Checkout:
        return KioskCheckout()

    def create_notification(self) -> Notification:
        return KioskNotification()