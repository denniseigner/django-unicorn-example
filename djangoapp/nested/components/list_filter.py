from django_unicorn.components import UnicornView


class ListFilterView(UnicornView):
    search = ""

    def updated_search(self, query):
        self.parent.parent.load_items(query)
        self.parent.parent.force_render = True
