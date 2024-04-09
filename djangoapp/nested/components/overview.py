from django_unicorn.components import UnicornView

from nested.models import ListItem


class OverviewView(UnicornView):
    list_items = ListItem.objects.none()

    def mount(self):
        self.load_items()

    def load_items(self, query=None):
        if query:
            self.list_items = ListItem.objects.filter(name__startswith=query)
        else:
            self.list_items = ListItem.objects.all()
        