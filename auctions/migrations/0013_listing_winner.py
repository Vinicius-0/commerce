# Generated by Django 3.2.9 on 2021-11-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20211120_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='winner',
            field=models.CharField(max_length=64, null=True),
        ),
    ]