from django import template

register = template.Library()

censor_list = ['повесился']


@register.filter()
def censor(value):
    for census in censor_list:
        value = value.replace(census[1:], '*' * len(census[1:]))
    return value
