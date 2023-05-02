from django import template
from animals.models import *


register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('animals/categories.html')
def show_categories():
    return {'categories': get_categories}
