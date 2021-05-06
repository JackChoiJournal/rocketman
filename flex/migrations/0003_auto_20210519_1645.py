# Generated by Django 2.2.21 on 2021-05-19 07:15

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0002_flexpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Blod title text for this card. Max length of 100 characters.', max_length=100)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional text for this card. Max length of 255 characters.', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be automatically cropped 570px by 370px')), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='More Detail', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))], help_text='Enter a link'))])))])), ('image_and_text', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image the automagically cropped to 786px by 552px')), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Image to the left'), ('right', 'Image to the right')], help_text='Image on the left with tet on the right. Vice versa')), ('title', wagtail.core.blocks.CharBlock(help_text='Max length of 60 characters.', max_length=60)), ('text', wagtail.core.blocks.CharBlock(max_length=140, required=False)), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='More Detail', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Max length of 200 characters.', max_length=200)), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='More Detail', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])), ('testimonial', wagtail.snippets.blocks.SnippetChooserBlock(target_model='testimonials.Testimonials', template='streams/testimonial_block.html')), ('pricing_table', streams.blocks.PricingTableBlock(table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': ['row_above', 'row_below', '---------', 'col_left', 'col_right', '---------', 'remove_row', 'remove_col', '---------', 'undo', 'redo'], 'editor': 'text', 'height': 108, 'minSpareRows': 0, 'renderer': 'text', 'rowHeaders': True, 'startCols': 4, 'startRows': 4, 'stretchH': 'all'})), ('richtext', wagtail.core.blocks.RichTextBlock())], blank=True, null=True),
        ),
    ]