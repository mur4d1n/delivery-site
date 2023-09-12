from django.db import models
from django.contrib.auth.models import User


class Provider(User):
    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'

    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Consumer(User):
    class Meta:
        verbose_name = 'Consumer'
        verbose_name_plural = 'Consumers'

    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    address = models.TextField(default='')
    geo_location = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    name = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='product', null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.name, self.category)


class Store(models.Model):
    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

    price = models.DecimalField(max_digits=8, decimal_places=2)

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)


class Order(models.Model):
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    STATUS = (
        ('new', 'new order'),
        ('pending', 'pending order'),
        ('finished', 'finished order')
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, default='new', choices=STATUS)

    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE, null=True, blank=True)


class OrderProduct(models.Model):
    class Meta:
        verbose_name = 'Product order'
        verbose_name_plural = 'Product orders'

    amount = models.IntegerField(default=0)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)