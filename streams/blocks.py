from django import forms
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock

class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required=True,
        help_text='Text to display',
    )

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"
        help_text = "Centered text to display on the page"


class LinkValue(blocks.StructValue):
    """Additional logic for the links"""

    def url(self) -> str:
        internal_page = self.get("internal_page")
        external_link = self.get("external_link")

        if internal_page:
            return internal_page.url
        elif external_link:
            return external_link

        return ""

from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

class Link(blocks.StructBlock):
    link_text = blocks.CharBlock(
        max_length=50,
        default="More Detail"
    )
    internal_page = blocks.PageChooserBlock(
        required=False
    )
    external_link = blocks.URLBlock(
        required=False
    )

    class Meta:
        value_class = LinkValue

    def clean(self, value):
        internal_page = value.get("internal_page")
        external_link = value.get("external_link")

        errors = {}

        if internal_page and external_link:
            errors["internal_page"] = ErrorList(["Both of these fields can't be filed. Please select one of these."])
            errors["external_link"] = ErrorList(["Both of these fields can't be filed. Please select one of these."])
        elif not internal_page and not external_link:
            errors["internal_page"] = ErrorList(["Please select at least one of these options."])
            errors["external_link"] = ErrorList(["Please select at least one of these options."])

        if errors:
            raise ValidationError("Validation error in your link", params=errors)
        return super().clean(value)

class Card(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=100,
        help_text="Blod title text for this card. Max length of 100 characters."
    )
    text = blocks.TextBlock(
        max_length=255,
        help_text="Optional text for this card. Max length of 255 characters.",
        required=False
    )
    image = ImageChooserBlock(
        help_text="Image will be automatically cropped 570px by 370px"
    )
    link = Link(help_text="Enter a link")

class CardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        Card()
    )

    class Meta:
        template = "streams/cards_block.html"
        icon = "image"
        label = "Standard Cards"

# class CardsBlock(blocks.StructBlock):
#     cards = blocks.ListBlock(
#         blocks.StructBlock([
#             ("title", blocks.CharBlock(max_length=100,
#                                        help_text="Blod title text for this card. Max length of 100 characters.")),
#             ("text",
#              blocks.TextBlock(max_length=255,
#                               help_text="Optional text for this card. Max length of 255 characters.",
#                               required=False)),
#             ("image", ImageChooserBlock(help_text="Image will be automatically cropped 570px by 370px"))
#         ])
#     )
#
#     class Meta:
#         template = "streams/cards_block.html"
#         icon = "image"
#         label = "Standard Cards"


class RadioSelectBlock(blocks.ChoiceBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field.widget = forms.RadioSelect(
            choices=self.field.widget.choices
        )

class ImageAndTextBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        help_text="Image the automagically cropped to 786px by 552px",
    )
    image_alignment = RadioSelectBlock(
        choices=(
            ("left", "Image to the left"),
            ("right", "Image to the right"),
        ),
        default="left",
        help_text="Image on the left with tet on the right. Vice versa"
    )
    title = blocks.CharBlock(
        max_length=60,
        help_text="Max length of 60 characters."
    )
    text = blocks.CharBlock(
        max_length=140,
        required=False,
    )
    link = Link()

    class Meta:
        template = "streams/image_and_text_block.html"
        icon = "image"
        label = "Image & text"

class CallToActionBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=200,
        help_text="Max length of 200 characters."
    )
    link = Link()

    class Meta:
        template = "streams/call_to_action_blcok.html"
        icon = "plus"
        label = "Call to action"

class PricingTableBlock(TableBlock):

    class Meta:
        template = "streams/pricing_table_block.html"
        icon = "table"
        label = "Pricing Table"
        help_text = "Your pricing tables should always 4 columns"

class RichTextWithTitleBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=50)
    context = blocks.RichTextBlock()

    class Meta:
        template = "streams/custom_simple_richtext_block.html"
