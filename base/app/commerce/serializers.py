from rest_framework import serializers
from commerce.models import Product, Payment, Order, Shipment

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class PaymentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ShipmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'