# Generated by Django 2.1.5 on 2019-02-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20190219_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='main',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
