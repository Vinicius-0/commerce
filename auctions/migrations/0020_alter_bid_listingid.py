# Generated by Django 3.2.9 on 2021-11-20 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_alter_listing_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='listingID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auctions.listing'),
        ),
    ]
