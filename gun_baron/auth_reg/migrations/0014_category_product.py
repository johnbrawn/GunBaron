# Generated by Django 2.1.5 on 2019-02-07 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_reg', '0013_auto_20190207_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('product_img', models.CharField(max_length=100)),
                ('product_desc', models.CharField(max_length=500)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_reg.Category')),
            ],
        ),
    ]
