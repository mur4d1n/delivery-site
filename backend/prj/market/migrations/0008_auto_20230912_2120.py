# Generated by Django 3.0.5 on 2023-09-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_orderproduct'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='consumer',
            options={'verbose_name': 'Consumer', 'verbose_name_plural': 'Consumers'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='orderproduct',
            options={'verbose_name': 'Product order', 'verbose_name_plural': 'Product orders'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='provider',
            options={'verbose_name': 'Provider', 'verbose_name_plural': 'Providers'},
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'verbose_name': 'Store', 'verbose_name_plural': 'Stores'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='product'),
        ),
    ]
