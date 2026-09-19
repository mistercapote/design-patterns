from domain.models import Order
from payments.processors import *

# Questão 03

def test_processamento_com_duas_formas_diferentes():
    order_pix = Order(150.0)
    order_card = Order(300.0)

    assert PixProcessor().process_order(order_pix) == "PIX"
    assert CreditCardProcessor().process_order(order_card) == "CREDIT_CARD"


def test_forma_de_pagamento_registada_no_pedido():
    order_pix = Order(50.0)
    order_boleto = Order(120.0)

    PixProcessor().process_order(order_pix)
    BoletoProcessor().process_order(order_boleto)

    assert order_pix.payment_method == "PIX"
    assert order_boleto.payment_method == "BOLETO"

