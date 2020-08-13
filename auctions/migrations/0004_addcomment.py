# Generated by Django 3.0.8 on 2020-08-13 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200813_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='addcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('content', models.CharField(max_length=128)),
                ('listingid', models.PositiveIntegerField()),
            ],
        ),
    ]
