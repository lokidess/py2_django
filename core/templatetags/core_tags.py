from django import template

from core.models import Post

register = template.Library()


@register.filter
def multi(value, x):
    return value * x


@register.filter
def alarm(value):
    return f"!!!{value}!!!"


@register.simple_tag
def formula(x, y, z):
    return x+y*z


@register.inclusion_tag('test_tpl.html')
def include_some():
    return {
        'post': Post.objects.all().last()
    }


@register.simple_tag
def queryset_filter(queryset, **kwargs):
    return queryset.filter(**kwargs).select_related()
