from django.db import models
from django.conf import settings



class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    weigth = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f'name:{self.name}'

class Payment(models.Model):
    
    PROCESSING = 'PR'
    PAID = 'PD'
    REJECTED = 'RJ'

    PAYMENT_CHOICES = [
        (PROCESSING, 'Processing'),
        (PAID, 'Paid'),
        (REJECTED, 'Rejected'),
    ]

    ammount = models.IntegerField(default=0)
    shipping_address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(
        max_length=2,
        choices=PAYMENT_CHOICES,
        default=PROCESSING,
    )
    orders = models.ManyToManyField('Order')
    def __str__(self):
        return f'status:{self.payment_status}'

class Order(models.Model):
    PENDING_PAYMENT = 'PP'
    PROCESSING = 'PR'
    ON_HOLD = 'OH'
    COMPLETED = 'CD'
    CANCELLED = 'CA'

    ORDER_CHOICES = [
        (PENDING_PAYMENT, 'Pending Payment'),
        (PROCESSING, 'Processing'),
        (ON_HOLD, 'On Hold'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    ammount = models.IntegerField(default=0)
    shipping_address = models.CharField(max_length=255)
    order_address = models.CharField(max_length=255)
    order_email = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    order_update = models.DateTimeField(auto_now=True)
    order_status = models.CharField(
        max_length=2,
        choices=ORDER_CHOICES,
        default=PROCESSING,
    )
    products = models.ManyToManyField(Product)
    payments = models.ManyToManyField(Payment)
    def __str__(self):
        return f'state:{self.order_status}'

class Shipment(models.Model):
    PROCESSING = 'PR'
    SENDING = 'OH'
    RECEIVED = 'CD'

    SHIPMENT_CHOICES = [
        (PROCESSING, 'Processing'),
        (SENDING, 'Sending'),
        (RECEIVED, 'Received'),
    ]
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    price = models.IntegerField(default=0)
    weigth = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    shipment_status = models.CharField(
        max_length=2,
        choices=SHIPMENT_CHOICES,
        default=PROCESSING,
    )
    shipping_address = models.CharField(max_length=255)
    def __str__(self):
        return f'status:{self.shipment_status}'