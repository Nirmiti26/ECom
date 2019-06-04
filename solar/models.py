from django.db import models

from config import UPLOAD_TO


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=100, null=False, blank=False)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    product_image = models.ImageField(upload_to=UPLOAD_TO, null=False, blank=False)
    product_manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    property_name = models.CharField(max_length=100)
    property_description = models.CharField(max_length=100)

    def __str__(self):
        return self.property_name


class Option(models.Model):
    option_name = models.CharField(max_length=20)

    def __str__(self):
        return self.option_name


class ProductOption(models.Model):
    options_id = models.ForeignKey(Option)
    product_id = models.ForeignKey(Product)

    def __str__(self):
        return "Option ID: ", self.options_id, " Product ID: ", self.product_id


class User(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    emailVerified = models.SmallIntegerField()
    registrationdate = models.DateField(auto_now=False, auto_now_add=True)
    user_ip = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.email


class Order(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    order_date = models.DateField(auto_now=False, auto_now_add=True)
    order_shipped = models.IntegerField()
    trackingNo = models.CharField(max_length=100)
    shipping_method = models.CharField(max_length=50)
    order_user_id = models.IntegerField()

    def __str__(self):
        return self.order_id


class OrderDetail(models.Model):
    order_id = models.ForeignKey(Option)
    product_id = models.ForeignKey(Product)
    order_no = models.IntegerField()
    price = models.FloatField()
    quantity = models.IntegerField()
    total_cost = models.FloatField()
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    fulfiled = models.SmallIntegerField()
    shipping_date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.order_id


class Shipping(models.Model):
    shipping_method = models.CharField(max_length=10)
    shipping_cost = models.FloatField
    shipping_duration = models.IntegerField()
    shipping_date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.shipping_method


class Payment(models.Model):
    payment_id = models.IntegerField()
    payment_type = models.CharField(max_length=10)
    order_detail_id = models.ForeignKey(OrderDetail)

    def __str__(self):
        return self.payment_id


class CardDetail(models.Model):
    credit_username = models.CharField(max_length=50)
    card_no = models.IntegerField()
    card_type = models.CharField(max_length=15)
    user_id = models.ForeignKey(User)

    def __str__(self):
        return self.credit_username


class ShoppingCart(models.Model):
    cart_details = models.TextField()
    product_id = models.ForeignKey(Product)
    user_id = models.ForeignKey(User)
    quantity = models.IntegerField()
    products_added = models.IntegerField()

    def __str__(self):
        return self.cart_details
