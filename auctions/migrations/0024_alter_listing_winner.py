# Generated by Django 3.2.9 on 2021-11-20 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_alter_bid_listingid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
