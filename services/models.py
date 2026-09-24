from channels.registry import get_channel_factory
from domain.builder import OrderBuilder
from domain.models import Product

class OrderService:
    def __init__(self,payment_processor, id_canal: str ):
        self.payment_processor= payment_processor
        self.channel_factory = get_channel_factory(id_canal)


    def execute(self, customer: str, products: Product):
        builder = OrderBuilder().set_customer(customer)
                
        for p in products:
            builder.add_product(p)
            
        pedido = builder.build()

        checkout = self.channel_factory.create_checkout()
        notificacao = self.channel_factory.create_notification()

        metodo_usado = self.payment_processor.process_order(pedido)
        
        # Junta o nome de todos os produtos
        nomes_produtos = ", ".join([p.name for p in pedido.products])
        
        # Print completo do resumo final
        print(f"\n--- Transação efetuada com sucesso! ---"
              f"\n{checkout.show(pedido)}"
              f"\nCliente: {pedido.customer}"
              f"\nProduto(s): {nomes_produtos}"
              f"\nTotal Pago: R${pedido.total():.2f}"
              f"\nMétodo: {metodo_usado}"
              f"\n{notificacao.send(pedido)}"
              f"\n---------------------------------------\n"
        )

