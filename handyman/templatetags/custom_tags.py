from django import template
from handyman.models import Skills

register = template.Library()


@register.simple_tag
def get_all_skills():
    return Skills.objects.all()
