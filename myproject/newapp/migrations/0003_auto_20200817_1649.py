# Generated by Django 3.1 on 2020-08-17 15:49

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import newapp.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('newapp', '0002_newpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpage',
            name='content',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('title_And_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True, validators=[newapp.blocks.check_for_title])), ('text', wagtail.core.blocks.RichTextBlock(features=['p', 'bold', 'ol'], required=True))]))], blank=True, null=True),
        ),
        migrations.CreateModel(
            name='NewPageImageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('carousel_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel_iamges', to='newapp.newpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]