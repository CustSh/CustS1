from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    # video = models.FileField(upload_to='products/video/', blank=True, null=True)  # новое поле для видео

    def __str__(self):
        return self.name

class Video(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="videos")
    file = models.FileField(upload_to='products/video/')
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "Видео для продукта " + str(self.product)