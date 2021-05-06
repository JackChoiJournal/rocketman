from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.core.fields import RichTextField


@register_setting
class HoursSettings(BaseSetting):
    hours = RichTextField(
        blank=True,
        null=True,
        features=[]
    )

    panels = [
        FieldPanel("hours")
    ]

    def save(self, *args, **kwargs):
        key = make_template_fragment_key("footer_hours_settings")
        cache.delete(key)

        return super().save(*args, **kwargs)

@register_setting
class ContactSetting(BaseSetting):
    contact = RichTextField(
        blank=True,
        null=True,
        features=["link"]
    )

    panels = [
        FieldPanel("contact")
    ]

    def save(self, *args, **kwargs):
        key = make_template_fragment_key("footer_contact_settings")
        cache.delete(key)

        return super().save(*args, **kwargs)


@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(
        blank=True,
        help_text="Enter your Facebook URL."
    )
    twitter = models.URLField(
        blank=True,
        help_text="Enter your Twitter URL."
    )
    youtube = models.URLField(
        blank=True,
        help_text="Enter your Youtube URL."
    )
    instagram = models.URLField(
        blank=True,
        help_text="Enter your Instagram URL."
    )

    panels = [
        FieldPanel("facebook"),
        FieldPanel("twitter"),
        FieldPanel("youtube"),
        FieldPanel("instagram"),
    ]

    def save(self, *args, **kwargs):
        key = make_template_fragment_key("footer_social_settings")
        cache.delete(key)

        return super().save(*args, **kwargs)
