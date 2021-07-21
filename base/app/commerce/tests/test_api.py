# Django
from django.urls import reverse
from django.contrib.auth import get_user_model
# Django Rest Framework
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

# models
from commerce.models import Order, Payment, Product, Shipment

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
def sample_product(name, price, weight):
    return Product.objects.create(
        name = name,
        price = price,
        weigth = weight
    )

class TestProductsAPI(APITestCase):

    def setUp(self):

        self.user = create_user(email='test@test.com', password='testpass')
        self.order = sample_order(self.user, 10000, 'av 123', 'av 123')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        

    def test_post_request_can_create_new_Product(self):
        payload = {
            "name": "airFryer",
            "price": 100,
            "weigth": 3,
            "description": "n/a",
            "stock": 2
        }
        request = self.client.post(reverse("commerce:product-list"), data=payload)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
    
    def test_post_request_can_create_new_Payment(self):
        payload = {
            "ammount": 1000,
            "shipping_address": "av 123",
            "payment_status": "PD",
        }
        request = self.client.post(reverse("commerce:payment-list"), data=payload)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.count(), 1)

    
