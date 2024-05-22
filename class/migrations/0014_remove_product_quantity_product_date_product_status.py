# Generated by Django 5.0.6 on 2024-05-18 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0013_alter_orderdetail_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
