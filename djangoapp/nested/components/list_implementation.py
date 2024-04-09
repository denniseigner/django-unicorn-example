from django_unicorn.components import UnicornView

from nested.models import ListItem


class ListImplementationView(UnicornView):
    list_items = ListItem.objects.none()

    def mount(self):
        pass
