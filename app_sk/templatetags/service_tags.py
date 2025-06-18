from django import template

register = template.Library()

@register.filter
def get_service_icon(value):
    icons = {
        1: 'hospital',
        2: 'user-md',
        3: 'pills',
        4: 'stethoscope',
        5: 'heartbeat',
    }
    return icons.get(value, 'medkit')