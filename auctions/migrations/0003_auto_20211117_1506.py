# Generated by Django 3.2.9 on 2021-11-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bids_comments_listings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=64)),
                ('title', models.CharField(default='', max_length=64)),
                ('listingID', models.IntegerField(default='')),
                ('bid', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('comment', models.CharField(default='', max_length=512)),
                ('listingID', models.IntegerField(default='')),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('category', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=512, null=True)),
                ('image', models.TextField(max_length=512, null=True)),
                ('initialBid', models.FloatField()),
                ('actualBid', models.FloatField(null=True)),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Bids',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Listings',
        ),
    ]
