from tutorial.quickstart.models import Customer, Seller, Item, Order, Warehouse
from rest_framework import viewsets
from tutorial.quickstart.serializers import CustomerSerializer, SellerSerializer, ItemSerializer, OrderSerializer, WarehouseSerializer
# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class SellerViewSet(viewsets.ModelViewSet):
	queryset = Seller.objects.all()
	serializer_class = SellerSerializer

class ItemViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

class WarehouseViewSet(viewsets.ModelViewSet):
	queryset = Warehouse.objects.all()
	serializer_class = WarehouseSerializer