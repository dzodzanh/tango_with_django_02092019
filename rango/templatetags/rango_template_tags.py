from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list():
    category_list = Category.objects.all()
    return {'cats': category_list}