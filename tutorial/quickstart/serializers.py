from rest_framework import serializers
from tutorial.quickstart.models import Customer, Seller, Item, Order, Warehouse

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Customer
		fields = ('id_customer', 'username', 'name', 'email', 'alamat', 'notelp')

class SellerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Seller
		fields = ('id_seller', 'username', 'name', 'email', 'alamat', 'notelp')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Item
		fields = ('id_item', 'name', 'description', 'price', 'stock', 'kategori', 'jenis', 'weight', 'place', 'id_seller')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Order
		fields = ('order_id', 'sent_to', 'status', 'id_seller', 'id_customer')

class WarehouseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Warehouse
		fields = ('warehouse_id', 'name', 'item_id')