from channels.base import ChannelFactory, Checkout, Notification
from channels.web import WebFactory, WebCheckout, WebNotification
from channels.mobile import MobileFactory, MobileCheckout, MobileNotification
from domain.models import Product, Order
from payments.processors import PixProcessor, CreditCardProcessor

# Questão 04

def simular_atendimento_canal(factory: ChannelFactory, order: Order) -> tuple[str, str]:
    """Função cliente que opera unicamente sobre as abstrações."""
    checkout: Checkout = factory.create_checkout()
    notification: Notification = factory.create_notification()

    mensagem_checkout = checkout.show(order)
    mensagem_notificacao = notification.send(order)
    return mensagem_checkout, mensagem_notificacao


def test_criacao_familia_web():
    """Valida a criação da família correspondente pela WebFactory."""
    factory = WebFactory()
    checkout = factory.create_checkout()
    notification = factory.create_notification()

    assert isinstance(checkout, WebCheckout), "Deveria criar um WebCheckout."
    assert isinstance(notification, WebNotification), "Deveria criar uma WebNotification."


def test_criacao_familia_mobile():
    """Valida a criação da família correspondente pela MobileFactory."""
    factory = MobileFactory()
    checkout = factory.create_checkout()
    notification = factory.create_notification()

    assert isinstance(checkout, MobileCheckout), "Deveria criar um MobileCheckout."
    assert isinstance(notification, MobileNotification), "Deveria criar uma MobileNotification."


def test_independencia_canal_e_pagamento():
    """Demonstra que canal e pagamento são independentes (WEB com PIX e MOBILE com Cartão)."""
    produto = Product("Produto A", 100.0)

    # Canal WEB com PIX
    pedido_web = Order(customer="Ana", products=[produto])
    PixProcessor().process_order(pedido_web)
    msg_checkout_web, msg_notif_web = simular_atendimento_canal(WebFactory(), pedido_web)

    assert pedido_web.payment_method == "PIX"
    assert "Web" in msg_checkout_web
    assert "Web" in msg_notif_web

    # Canal MOBILE com Cartão de Crédito
    pedido_mobile = Order(customer="Carlos", products=[produto])
    CreditCardProcessor().process_order(pedido_mobile)
    msg_checkout_mobile, msg_notif_mobile = simular_atendimento_canal(MobileFactory(), pedido_mobile)

    assert pedido_mobile.payment_method == "CREDIT_CARD"
    assert "Mobile" in msg_checkout_mobile
    assert "Mobile" in msg_notif_mobile


if __name__ == "__main__":
    test_criacao_familia_web()
    test_criacao_familia_mobile()
    test_independencia_canal_e_pagamento()
    print("Testes da Questão 04 (Abstract Factory) passaram com sucesso!")
