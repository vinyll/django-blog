from django import template
from django.conf import settings
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag
def analytics():
    key = getattr(settings, 'GOOGLE_ANALYTICS_KEY')
    if key:
        return render_to_string('partials/analytics.html', locals())
    return ''