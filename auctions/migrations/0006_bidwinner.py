# Generated by Django 3.0.8 on 2020-08-13 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_addbid'),
    ]

    operations = [
        migrations.CreateModel(
            name='bidwinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(max_length=64)),
                ('winner', models.CharField(max_length=64)),
                ('listingid', models.PositiveIntegerField()),
                ('finalbid', models.IntegerField()),
            ],
        ),
    ]
