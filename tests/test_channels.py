from channels.registry import get_channel_factory, register_channel_factory
from channels.web import WebFactory, WebCheckout, WebNotification
from channels.mobile import MobileFactory, MobileCheckout, MobileNotification
from channels.kiosk import KioskFactory, KioskCheckout, KioskNotification

# Questão 05

def test_canais_iniciais_web_e_mobile():
    web_factory = get_channel_factory("WEB")
    assert isinstance(web_factory, WebFactory)
    assert isinstance(web_factory.create_checkout(), WebCheckout)
    assert isinstance(web_factory.create_notification(), WebNotification)

    mobile_factory = get_channel_factory("MOBILE")
    assert isinstance(mobile_factory, MobileFactory)
    assert isinstance(mobile_factory.create_checkout(), MobileCheckout)
    assert isinstance(mobile_factory.create_notification(), MobileNotification)


def test_canal_desconhecido_produz_erro():
    try:
        get_channel_factory("DESCONHECIDO")
        assert False, "Deveria ter lancado ValueError para canal desconhecido."
    except ValueError as e:
        assert "Canal desconhecido: 'DESCONHECIDO'" in str(e)

def test_adicao_dinamica_kiosk_sem_alterar_registro():
    # Registra a nova fábrica KIOSK externamente
    register_channel_factory("KIOSK", KioskFactory)

    # Recupera e testa sem ter modificado o interior de get_channel_factory
    kiosk_factory = get_channel_factory("KIOSK")
    assert isinstance(kiosk_factory, KioskFactory)
    assert isinstance(kiosk_factory.create_checkout(), KioskCheckout)
    assert isinstance(kiosk_factory.create_notification(), KioskNotification)


if __name__ == "__main__":
    test_canais_iniciais_web_e_mobile()
    test_canal_desconhecido_produz_erro()
    test_adicao_dinamica_kiosk_sem_alterar_registro()
    print("Todos os testes de canais e registro passaram com sucesso!")