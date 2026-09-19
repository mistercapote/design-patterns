from channels.registry import get_channel_factory, register_channel_factory
from channels.web import WebFactory, WebCheckout, WebNotification
from channels.mobile import MobileFactory, MobileCheckout, MobileNotification
from channels.kiosk import KioskFactory, KioskCheckout, KioskNotification

# Questao 05

def test_canais_iniciais_web_e_mobile():
    """Valida a recuperação das fábricas registradas inicialmente."""
    web_factory = get_channel_factory("WEB")
    assert isinstance(web_factory, WebFactory)
    assert isinstance(web_factory.create_checkout(), WebCheckout)
    assert isinstance(web_factory.create_notification(), WebNotification)

    mobile_factory = get_channel_factory("MOBILE")
    assert isinstance(mobile_factory, MobileFactory)
    assert isinstance(mobile_factory.create_checkout(), MobileCheckout)
    assert isinstance(mobile_factory.create_notification(), MobileNotification)


def test_canal_desconhecido_produz_erro():
    """Valida que uma consulta por canal não registrado produz erro claro."""
    try:
        get_channel_factory("DESCONHECIDO")
        assert False, "Deveria ter lançado ValueError para canal desconhecido."
    except ValueError as e:
        assert "Canal desconhecido: 'DESCONHECIDO'" in str(e)


def test_adicao_dinamica_kiosk_sem_alterar_registro():
    """Valida a adição de KIOSK via registro externo, preservando o OCP."""
    register_channel_factory("KIOSK", KioskFactory)

    kiosk_factory = get_channel_factory("KIOSK")
    assert isinstance(kiosk_factory, KioskFactory)
    assert isinstance(kiosk_factory.create_checkout(), KioskCheckout)
    assert isinstance(kiosk_factory.create_notification(), KioskNotification)


if __name__ == "__main__":
    test_canais_iniciais_web_e_mobile()
    test_canal_desconhecido_produz_erro()
    test_adicao_dinamica_kiosk_sem_alterar_registro()
    print("Testes da Questão 05 (Seleção e Registro OCP) passaram com sucesso!")
