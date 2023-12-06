from django import template
from ..models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    menu_items = MenuItem.objects.filter(parent__isnull=True, title=menu_name).prefetch_related('children')

    def is_current(item):
        return current_path.startswith(item.url)

    def render_menu(menu_items):
        result = []
        for item in menu_items:
            is_active = is_current(item)
            result.append({
                'title': item.title,
                'url': item.url,
                'is_active': is_active,
                'children': render_menu(item.children.all()) if is_active else []
            })
        return result

    return render_menu(menu_items)
