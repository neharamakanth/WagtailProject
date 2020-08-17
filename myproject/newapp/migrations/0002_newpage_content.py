# Generated by Django 3.1 on 2020-08-17 13:01

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_And_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('text', wagtail.core.blocks.TextBlock(required=True))]))], blank=True, null=True),
        ),
    ]
