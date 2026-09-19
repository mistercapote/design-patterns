from domain.models import Product
from domain.builder import OrderBuilder

# Questão 02

def test_construcao_pedido_com_dois_ou_mais_produtos():
    """Demonstra a construção de um pedido com pelo menos dois produtos e valida o total."""
    p1 = Product(name="Teclado Mecânico", price=350.00)
    p2 = Product(name="Mouse sem fio", price=150.00)

    order = (
        OrderBuilder()
        .set_customer("Luiz")
        .add_product(p1)
        .add_product(p2)
        .build()
    )

    assert len(order.products) == 2, "O pedido deve conter exatamente 2 produtos."
    assert order.total() == 500.00, f"O total esperado é 500.00, obtido {order.total()}"


def test_utilizacao_de_atributos_opcionais():
    """Demonstra a utilização de pelo menos dois atributos opcionais (ex.: endereço e cupom)."""
    p1 = Product(name="Headphone", price=250.00)

    order = (
        OrderBuilder()
        .set_customer("Eduardo")
        .add_product(p1)
        .set_address("Rua das Palmeiras, 123")
        .set_coupon("DESC10")
        .set_observation("Entregar na portaria")
        .build()
    )

    assert order.address == "Rua das Palmeiras, 123"
    assert order.coupon == "DESC10"
    assert order.observation == "Entregar na portaria"


def test_rejeicao_construcao_sem_cliente():
    """Demonstra a tentativa de construir um pedido sem cliente disparando erro."""
    p1 = Product(name="Monitor", price=1200.00)
    builder = OrderBuilder().add_product(p1)

    try:
        builder.build()
        assert False, "Deveria ter levantado ValueError por ausência de cliente."
    except ValueError as e:
        assert "sem cliente" in str(e)


if __name__ == "__main__":
    test_construcao_pedido_com_dois_ou_mais_produtos()
    test_utilizacao_de_atributos_opcionais()
    test_rejeicao_construcao_sem_cliente()
    print("Todos os testes do Builder passaram com sucesso!")


