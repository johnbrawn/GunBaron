# Generated by Django 2.1.5 on 2019-02-07 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_reg', '0011_category_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.EmailField(max_length=254),
        ),
    ]
