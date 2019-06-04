from django.contrib import admin

from solar.models import *


class manufacturer(admin.ModelAdmin):
    class Meta:
        model = Manufacturer


admin.site.register(Manufacturer, manufacturer)


class product(admin.ModelAdmin):
    class Meta:
        model = Product


admin.site.register(Product, product)


class productSpecification(admin.ModelAdmin):
    class Meta:
        model = ProductSpecification


admin.site.register(ProductSpecification, productSpecification)


class option(admin.ModelAdmin):
    class Meta:
        model = Option


admin.site.register(Option, option)


class productOption(admin.ModelAdmin):
    class Meta:
        model = ProductOption


admin.site.register(ProductOption, productOption)


class user(admin.ModelAdmin):
    class Meta:
        model = User


admin.site.register(User, user)


class order(admin.ModelAdmin):
    class Meta:
        model = Order


admin.site.register(Order, order)


class orderDetail(admin.ModelAdmin):
    class Meta:
        model = OrderDetail


admin.site.register(OrderDetail, orderDetail)


class shipping(admin.ModelAdmin):
    class Meta:
        model = Shipping


admin.site.register(Shipping, shipping)


class payment(admin.ModelAdmin):
    class Meta:
        model = Payment


admin.site.register(Payment, payment)


class cardDetail(admin.ModelAdmin):
    class Meta:
        model = CardDetail


admin.site.register(CardDetail, cardDetail)


class shoppingCart(admin.ModelAdmin):
    class Meta:
        model = ShoppingCart


admin.site.register(ShoppingCart, shoppingCart)
