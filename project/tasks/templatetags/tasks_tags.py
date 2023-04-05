from django import template

register = template.Library()

@register.simple_tag
def normalize_status(status: bool) -> str:
    return "Выполнено" if status == True else "Не выполнено"