# Generated by Django 5.1.2 on 2024-11-14 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_category_slug_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Скидка в %'),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество'),
        ),
    ]