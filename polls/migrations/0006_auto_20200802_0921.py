# Generated by Django 3.0.8 on 2020-08-02 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_product_product_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_seller',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='product_buyer',
        ),
        migrations.AddField(
            model_name='cart',
            name='product_name',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='seller',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='buyer',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Cart'),
        ),
        migrations.AddField(
            model_name='user',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Orders'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product_qentity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cart',
            name='state',
            field=models.IntegerField(default=1),
        ),
    ]
