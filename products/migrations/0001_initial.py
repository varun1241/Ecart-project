# Generated by Django 4.0 on 2023-01-10 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('strap_color', models.CharField(max_length=100)),
                ('highlights', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='product')),
                ('status', models.BooleanField()),
            ],
        ),
    ]
