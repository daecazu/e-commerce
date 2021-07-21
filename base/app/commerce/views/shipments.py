from rest_framework import viewsets
from commerce.models import Shipment
from commerce.serializers import ShipmentModelSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ShipmentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Shipment.objects.all()
    serializer_class = ShipmentModelSerializer