from domain.models import Order, Product

# Questão 02 

class OrderBuilder:
    def __init__(self):
        self._customer = None
        self._products = []
        self._address = None
        self._coupon = None
        self._payment_method = None
        self._observation = None

    def set_customer(self, customer: str):
        self._customer = customer
        return self

    def add_product(self, product: Product):
        self._products.append(product)
        return self

    def set_address(self, address: str):
        self._address = address
        return self

    def set_coupon(self, coupon: str):
        self._coupon = coupon
        return self

    def set_payment_method(self, payment_method: str):
        self._payment_method = payment_method
        return self

    def set_observation(self, observation: str):
        self._observation = observation
        return self

    def build(self) -> Order:
        if not self._customer:
            raise ValueError("Não é possível construir um pedido sem cliente.")

        return Order(
            customer=self._customer,
            products=self._products,
            address=self._address,
            coupon=self._coupon,
            payment_method=self._payment_method,
            observation=self._observation,
        )
