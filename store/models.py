from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, CharField, EmailField, FloatField, BooleanField, ForeignKey, \
    SET_NULL, DateTimeField, IntegerField, ImageField


class Customer(Model):
    user = OneToOneField(User, CASCADE, null=True, blank=True)
    name = CharField(max_length=255, null=True)
    email = EmailField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=255, null=True)
    price = FloatField()
    digital = BooleanField(default=False, null=True, blank=False)
    image = ImageField(upload_to='products/', default='apps/static/store/images/placeholder.png')

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name


class Order(Model):
    customer = ForeignKey(Customer, SET_NULL, null=True, blank=True)
    complete = BooleanField(default=False)
    transaction_id = CharField(max_length=255, blank=True)
    date_ordered = DateTimeField(auto_now_add=True)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        return sum(i.get_total for i in order_items)

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        return sum(i.quantity for i in order_items)

    def __str__(self):
        return f'{self.id}'


class OrderItem(Model):
    product = ForeignKey(Product, SET_NULL, null=True)
    order = ForeignKey(Order, SET_NULL, null=True)
    quantity = IntegerField(default=0, null=True, blank=True)
    date_added = DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.product.price * self.quantity


class ShippingAddress(Model):
    customer = ForeignKey(Customer, SET_NULL, null=True)
    order = ForeignKey(Order, SET_NULL, null=True)
    address = CharField(max_length=255, null=True)
    city = CharField(max_length=255, null=True)
    state = CharField(max_length=255, null=True)
    zipcode = CharField(max_length=255, null=True)
    date_added = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
