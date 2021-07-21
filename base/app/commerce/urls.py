from django.urls import path
from commerce.views.products import ProductViewSet




router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]
