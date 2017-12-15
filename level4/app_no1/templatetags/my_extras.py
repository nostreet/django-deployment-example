from django import template

register = template.Library()

@register.filter(name='snippy')
def snippy(value,arg):
    """
    this cuts out all values of arg from the string
    """
    return value.replace(arg,'')
