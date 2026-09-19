# Questão 02

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class Order:
    def __init__(
        self,
        customer: str,
        products: list[Product] = None,
        address: str = None,
        coupon: str = None,
        payment_method: str = None,
        observation: str = None,
    ):
        self.customer = customer
        self.products = products if products is not None else []
        self.address = address
        self.coupon = coupon
        self.payment_method = payment_method
        self.observation = observation

    def total(self) -> float:
        """Devolve a soma dos preços de todos os produtos."""
        return sum(p.price for p in self.products)
