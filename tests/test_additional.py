from config.appconfig import AppConfig
from domain.builder import OrderBuilder
from channels.kiosk import KioskFactory

#  Questão 7

def test_double_config():
    """Testa se obter AppConfig resulta  em uma única instância
    
    Se as instâncias forem idênticas, o teste passa silenciosamente
    e a função não retorna nada
    
    e o sistema permitisse instâncias diferentes, teríamos inconsistências 
    graves, pois cada módulo poderia estar a usar parâmetros e variáveis 
    distintas, gerando conflitos e erros imprevisíveis
    """

    config1 = AppConfig()
    config2 = AppConfig()


    assert config1 is config2, "Deve haver apenas uma instância de AppConfig"

def test_builder_empty_product_list():
    """
    Criação de um pedido fornecendo apenas o atributo 
    obrigatório (cliente), sem adicionar produtos. 
    """
    try: 
        order= (
            OrderBuilder()
            .set_customer('Jaime')
            .build()
        )
    except ValueError as e:
        assert "O pedido deve conter pelo menos um produto" in str(e)




def test_different_kiosk_factory_checkout_instances():

    factory = KioskFactory()
    checkout1 = factory.create_checkout()
    checkout2 = factory.create_checkout()

    assert checkout1 is not checkout2, 'Checkout diferentes são instâncias diferentes'


if __name__ == "__main__":
    test_double_config()
    test_builder_empty_product_list()
    test_different_kiosk_factory_checkout_instances()
    print("Todos os testes do Builder passaram com sucesso!")