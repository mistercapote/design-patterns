from services.models import OrderService
from domain.models import Product
from payments.processors import PixProcessor, CreditCardProcessor, DebitCardProcessor, BoletoProcessor

if __name__ == "__main__":
    processor_pix = PixProcessor()
    service_web = OrderService(payment_processor=processor_pix, id_canal="WEB")
    produto_1 = Product(name="Notebook M1", price=7500.00)
    
    service_web.execute(customer="João Silva", products=[produto_1])

    processor_credito = CreditCardProcessor()
    service_mobile = OrderService(payment_processor=processor_credito, id_canal="MOBILE")
    produto_2 = Product(name="Smartphone", price=3500.00)
    
    service_mobile.execute(customer="Maria Souza", products=[produto_2])

    processor_debito = DebitCardProcessor()
    service_kiosk = OrderService(payment_processor=processor_debito, id_canal="KIOSK")
    produto_3 = Product(name="Fone Bluetooth", price=500.00)
    produto_4 = Product(name="Teclado Mecânico", price=350.00)
    produto_5 = Product(name="Mouse Gamer", price=250.00)
    service_kiosk.execute(customer="Carlos Mendes", products=[produto_3, produto_4, produto_5])
