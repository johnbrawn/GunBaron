# Generated by Django 2.1.5 on 2019-03-05 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190305_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, default='New', null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Status'),
        ),
    ]
