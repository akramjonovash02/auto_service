# Generated by Django 5.0.7 on 2024-07-30 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'confirmate is pending'), ('2', 'is being collected'), ('3', 'is being delivered'), ('4', 'successfully'), ('5', 'canceled')], max_length=50)),
                ('payment_type', models.CharField(choices=[('CASH', 'CASH'), ('CARD', 'CARD')], max_length=10)),
                ('order_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'confirmate is pending'), ('2', 'is being collected'), ('3', 'is being delivered'), ('4', 'successfully'), ('5', 'canceled')], max_length=50)),
                ('payment_type', models.CharField(choices=[('CASH', 'CASH'), ('CARD', 'CARD')], max_length=10)),
            ],
        ),
    ]
