from config.appconfig import AppConfig

# Questão 01

def test_mesma_instancia():
    """Testa se duas chamadas a AppConfig devolvem exatamente o mesmo objeto."""
    config1 = AppConfig()
    config2 = AppConfig()
    assert config1 is config2, "config1 e config2 devem apontar para a mesma instância."


def test_propagacao_de_alteracoes():
    """Testa se uma alteração realizada numa referência é refletida na outra."""
    config1 = AppConfig()
    config2 = AppConfig()

    config1.debug = True
    config1.currency = "EUR"

    assert config2.debug is True, "A alteração em 'debug' deve ser observável em config2."
    assert config2.currency == "EUR", "A alteração em 'currency' deve ser observável em config2."


def test_preservacao_de_valores_ao_reobter():
    """Testa se uma nova chamada a AppConfig não restaura os valores predefinidos."""
    config1 = AppConfig()
    config1.environment = "staging"

    # Nova chamada para obter a configuração
    config2 = AppConfig()

    assert config2.environment == "staging", "O atributo 'environment' alterado não deve ser reinicializado."
    assert config2.debug is True, "O atributo 'debug' deve manter o estado previamente alterado."


# def executar_todos_os_testes():
#     test_mesma_instancia()
#     test_propagacao_de_alteracoes()
#     test_preservacao_de_valores_ao_reobter()
#     print("Todos os testes passaram com sucesso!")


# if __name__ == "__main__":
#     executar_todos_os_testes()