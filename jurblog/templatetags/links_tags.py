# -*- coding: utf-8 -*-
from django import template
from jurblog.models import Category

register = template.Library()

@register.inclusion_tag('jurblog/links.html')
def sidebar_links(index):
    categories = Category.objects.all()
    return {
        'categories': categories
    }
