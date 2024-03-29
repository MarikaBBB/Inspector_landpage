import logging

from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel("INFO")

DEFAULTS = {
    "Systems - read": {
        "system": ["view"],
        "environment": ["view"],
        "instance": ["view"],
        "dbtable": ["view"],
    },
    "Systems - edit": {
        "system": ["view", "add", "change", "delete"],
        "environment": ["view", "add", "change", "delete"],
        "instance": ["view", "add", "change", "delete"],
        "dbtable": ["view", "add", "change", "delete"],
    },
    "Checks - read": {"datacheck": ["view"], "checkrun": ["view"]},
    "Checks - edit": {
        "datacheck": ["view", "add", "change", "delete"],
        "checkrun": ["view", "add", "change", "delete"],
    },
    "Checks - run": {"datacheck": ["view"], "checkrun": ["view", "add"]},
    "Profiling - read": {"tableprofile": ["view"]},
    "Profiling - run": {"tableprofile": ["view", "add"]},
}


class Command(BaseCommand):
    help = "Creates default groups and permissions"

    def handle(self, *args, **kwargs):
        for group, models in DEFAULTS.items():
            new_group, created = Group.objects.get_or_create(name=group)
            for model, permissions in models.items():
                for permission in permissions:
                    codename = f"{permission}_{model}"

                    try:
                        model_add_perm = Permission.objects.get(codename=codename)
                    except Permission.DoesNotExist:
                        self.stderr.write(f"Permission not found: {codename}'.")
                        continue

                    self.stdout.write(f"Adding permission '{codename}' to group '{group}'")
                    new_group.permissions.add(model_add_perm)

        self.stdout.write("Created default groups and permissions.")
