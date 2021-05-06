from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.core.exceptions import ValidationError
from django.db import models
from django.forms.utils import ErrorList
from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.core.models import Orderable


class MenuItem(Orderable):
    link_title = models.CharField(max_length=50, blank=True)
    link_url = models.CharField(max_length=500, blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]

    page = ParentalKey("Menu", related_name="menu_item", on_delete=models.CASCADE)

    @property
    def url(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url

        return ""

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return "Missing title"

    def clean(self):
        link_url = self.link_url
        link_page = self.link_page

        errors = {}

        if link_url and link_page:
            errors["link_url"] = ErrorList("Please only select one of these options. link_url or link_page")
            errors["link_page"] = ErrorList("Please only select one of these options. link_url or link_page")

        if errors:
            raise ValidationError("Validation error in link.", params=errors)

class Menu(ClusterableModel):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(
        populate_from="title",
        editable=True,
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("slug"),
        # "menu_item" comes from related_name="menu_item"
        # of ParentalKey of MenuItem.
        InlinePanel("menu_item", label="Menu item")
    ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        key = make_template_fragment_key(
            "site_header",
            [self.id],
        )
        cache.delete(key)

        key = make_template_fragment_key(
            "site_footer",
            [self.id],
        )
        cache.delete(key)

        return super().save(*args, **kwargs)