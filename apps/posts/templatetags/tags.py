from django import template

from apps.posts.functions import obtenerCategorias

register = template.Library()

@register.simple_tag
def getCategorias():
    return obtenerCategorias()