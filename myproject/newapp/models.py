from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import InlinePanel,FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from newapp import blocks as newblocks
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

# Create your models here.

class NewPageImageGallery(Orderable):
    page=ParentalKey("newapp.NewPage",related_name="carousel_images")
    carousel_image=models.ForeignKey(
    "wagtailimages.Image",
    null=True,
    blank=False,
    on_delete=models.SET_NULL,
    related_name="+",
    )


panels=[
ImageChooserPanel("carousel_image")
]
class NewPage(Page):
    template="newapp/new_page.html"
    content=StreamField(
    [
        ('text', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ("title_And_text",newblocks.TitleAndTextBlock()),
        
    ],
    null=True,
    blank=True
    )

    subtitle=models.CharField(max_length=100,null=True,blank=True)
    content_panels=Page.content_panels+[
    FieldPanel("subtitle"),
    StreamFieldPanel("content"),
    InlinePanel("carousel_images"),
    ]

class Meta():
    verbose_name="New Page"
    verbose_name_plural="New Pages"
