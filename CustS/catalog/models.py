from django.db import models
from django.db.models import ForeignKey


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    def __str__(self):
        return self.name



class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    category = ForeignKey(to=Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'SubCategory'


class SubClass(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    category = ForeignKey(to=SubCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'SubClass'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

