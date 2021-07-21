from django.test import TestCase
from commerce.models import Order, Payment, Product, Shipment

from django.contrib.auth import get_user_model

def create_user(**params):
    """Helper to create users for our tests"""
    return get_user_model().objects.create_user(**params)

def sample_order(User, ammount, shipping_address, order_address):
    return Order.objects.create(
        user=User,
        ammount=ammount,
        shipping_address=shipping_address,
        order_address=order_address,
        order_email=User.email
    )

def sample_payment(ammount, shipping_address):
    return Payment.objects.create(
        ammount=ammount,
        shipping_address=shipping_address
    )

def sample_product(name, price, weight):
    return Product.objects.create(
        name = name,
        price = price,
        weigth = weight
    )

def sample_shipment(Order):
    return Shipment.objects.create(
        order = Order,
        shipping_address = Order.shipping_address
    )

class TestModels(TestCase):
    def setUp(self):
        self.user = create_user(email='test@test.com', password='testpass')
        self.order = sample_order(self.user, 10000, 'av 123', 'av 123')
        self.order2 = sample_order(self.user, 3000, 'av 123', 'av 123')
        self.product1 = sample_product('airfryer', 100, 3)
        self.product2 = sample_product('vertex v60', 100, 3)
        self.payment1 = sample_payment(5000, 'av 123')
        self.payment2 = sample_payment(4000, 'av 123')
        self.shipment1 = sample_shipment(self.order)

    def test_that_order_has_two_payments(self):
        """test many to many relation"""
        self.order.payments.add(self.payment1, self.payment2)
        self.assertEqual(self.order.payments.count(), 2)

    def test_that_payment_has_two_orders(self):
        """test many to many relation"""
        self.payment1.orders.add(self.order, self.order2)
        self.assertEqual(self.payment1.orders.count(), 2)
    
    def test_that_order_has_two_products(self):
        """test many to many relation"""
        self.order.products.add(self.product1, self.product2)
        self.assertEqual(self.order.products.count(), 2)
    
    def test_order_str(self):
        """test order str"""
        self.assertEqual(
            str(self.order),
            f'state:{self.order.order_status}'
        )

    def test_product_str(self):
        """test product str"""
        self.assertEqual(
            str(self.product1),
            f'name:{self.product1.name}'
        )

    def test_payment_str(self):
        """test payment str"""
        self.assertEqual(
            str(self.payment1),
            f'status:{self.payment1.payment_status}'
        )
    
    def test_shipment_str(self):
        """test shipment str"""
        self.assertEqual(
            str(self.shipment1),
            f'status:{self.shipment1.shipment_status}'
        )

