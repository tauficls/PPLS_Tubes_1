from django.db import models

# Create your models here.
class Customer(models.Model):
	id_customer = models.AutoField(primary_key=True)
	username = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	alamat = models.TextField()
	notelp = models.CharField(max_length=25)


class Seller(models.Model):
	id_seller = models.AutoField(primary_key=True)
	username = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	alamat = models.TextField()
	notelp = models.CharField(max_length=25)

class Item(models.Model):
	id_item = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	description = models.TextField()
	price = models.IntegerField(default=0)
	stock = models.IntegerField(default=0)
	kategori = models.CharField(max_length=25)
	jenis = models.CharField(max_length=25)
	weight = models.IntegerField(default=0)
	place = models.CharField(max_length=50)
	id_seller = models.IntegerField(max_length=50)

class Order(models.Model):
	order_id = models.AutoField(primary_key=True)
	sent_to = models.CharField(max_length=100)
	status = models.CharField(max_length=50)
	id_seller = models.IntegerField(max_length=50)
	id_customer = models.IntegerField(max_length=50)
	date_order = models.DateTimeField(auto_now_add=True)

class Warehouse(models.Model):
	warehouse_id = models.IntegerField(max_length=50)
	name = models.CharField(max_length=10)
	item_id = models.IntegerField(max_length=50)
