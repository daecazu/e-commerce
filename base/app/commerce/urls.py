from django.urls import include,path
from commerce.views.products import ProductViewSet
from commerce.views.payments import PaymentViewSet
from commerce.views.orders import OrderViewSet
from commerce.views.shipments import ShipmentViewSet

from rest_framework.routers import DefaultRouter


app_name ='commerce'
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'shipments', ShipmentViewSet, basename='shipment')


urlpatterns = [
    path('', include(router.urls)),
]
