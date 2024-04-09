from django.core.management.base import BaseCommand, CommandError
from nested.models import ListItem


class Command(BaseCommand):
    help = "Seed ListItems"

    def handle(self, *args, **options):
        for i in range(0, 10):
            list_item = ListItem(name=f"ExampleItem {i + 1}")
            list_item.save()

            list_item = ListItem(name=f"FunItem {i + 1}")
            list_item.save()

            list_item = ListItem(name=f"FilterItem {i + 1}")
            list_item.save()
