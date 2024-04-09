from django_unicorn.components import UnicornView

from nested.models import ListItem


class ListItemView(UnicornView):
    
    item : ListItem

    def mount(self):
        pass
