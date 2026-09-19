from channels.registry import get_channel_factory
from domain.builder import OrderBuilder
from domain.models import Product

class OrderService:
    def __init__(self,payment_processor, id_canal: str ):
        self.payment_processor= payment_processor
        self.channel_factory = get_channel_factory(id_canal)


    def execute(self, customer: str, product: Product):
        pedido = OrderBuilder().set_customer(customer).add_product(product).build()
        checkout = self.channel_factory.create_checkout() # exibir o checkou na tela
        checkout.show(pedido)

        # Processar o pagamento
        self.payment_processor.process_order(pedido)

        #  Parte da notificação
        notificacao = self.channel_factory.create_notification()
        notificacao.send(pedido)
