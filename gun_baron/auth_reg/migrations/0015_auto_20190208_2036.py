# Generated by Django 2.1.5 on 2019-02-08 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_reg', '0014_category_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
