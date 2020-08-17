from wagtail.core import blocks
from django.core.validators import ValidationError


def check_for_title(value):
    if 'the' in value:
        raise ValidationError('Title cannot contain the word "the"')


class TitleAndTextBlock(blocks.StructBlock):

      title=blocks.CharBlock(required=True,validators=[check_for_title],max_length=60)
      text=blocks.RichTextBlock(required=True,features=['p','bold','ol'])
      button_page=blocks.PageChooserBlock(required=False)
      button_url=blocks.URLBlock(required=False)
      button_text=blocks.CharBlock(required=True,default='Learn Wagtail',max_length=40)
      class Meta:
          template="newapp/title_text.html"
          icon="edit"
          lable="titleandtext"
