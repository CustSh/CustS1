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
    #quantity = models.PositiveIntegerField(default=0)
    #video = models.FileField(upload_to='products/video/', blank=True, null=True)  # поле для одного видео в карточке

    def sell_price(self):
        # if self.discount:
        #     return round(self.price - self.price*self.discount/100, 2)
        return self.price

    def __str__(self):
        return self.name



class Video(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="videos")
    file = models.FileField(upload_to='products/video/')
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "Видео для продукта " + str(self.product)