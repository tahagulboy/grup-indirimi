# Generated by Django 4.1.5 on 2023-06-10 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20210709_2210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name_plural': '1. Afişler'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': '3. Markalar'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '2. Kategoriler'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name_plural': '4. Renkler'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '6. Ürünler'},
        ),
        migrations.AlterModelOptions(
            name='productattribute',
            options={'verbose_name_plural': '7. Ürün Varyasyonları'},
        ),
        migrations.AlterModelOptions(
            name='productreview',
            options={'verbose_name_plural': 'Yorumlar'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name_plural': '5. Boyutlar'},
        ),
    ]
