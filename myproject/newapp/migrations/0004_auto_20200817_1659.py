# Generated by Django 3.1 on 2020-08-17 15:59

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_auto_20200817_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpageimagegallery',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel_images', to='newapp.newpage'),
        ),
    ]
