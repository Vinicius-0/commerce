# Generated by Django 3.2.9 on 2021-11-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_listing_initialbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='actualBid',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='listing',
            name='initialBid',
            field=models.FloatField(),
        ),
    ]