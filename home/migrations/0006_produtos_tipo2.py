# Generated by Django 4.2.9 on 2024-07-02 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='tipo2',
            field=models.CharField(default='', max_length=1000),
        ),
    ]