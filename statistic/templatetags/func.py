from django import template

register = template.Library()


@register.filter()
def sub(val1, val2):
    return str(float(val1)-float(val2))