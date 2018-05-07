from django import template

from cfp.utils import is_staff
from ponyconf.utils import markdown_to_html


register = template.Library()


@register.simple_tag
def markdown(value):
    return markdown_to_html(value)


@register.filter
def staff(request):
    return is_staff(request, request.user)


@register.filter(name='duration_format')
def duration_format(value):
    value = int(value)
    hours = int(value/60)
    minutes = value%60
    return '%d h %02d' % (hours, minutes)


@register.filter
def exclude(queryset, excluded):
    return queryset.exclude(pk=excluded.pk)
