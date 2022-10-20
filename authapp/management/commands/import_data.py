import json
import os

from django.core.management import BaseCommand

from authapp.models import TodoUser
from ToDoProject.settings import BASE_DIR


class Command(BaseCommand):
    def handle(self, *args, **options):
        super_user = TodoUser.objects.create_superuser('admin', 'admin@example.local', 'Qq123456')
        print(f'** user created ** ({super_user})')

        try:
            file_path = os.path.join(BASE_DIR, 'authapp', 'users_init.json')
            with open(file_path, 'r', encoding='utf-8') as read_file:
                data = json.load(read_file)

            if data['users']:
                for user in data['users']:
                    new_user, is_created = TodoUser.objects.get_or_create(**user)
                    if is_created:
                        new_user.save()
                        print(f'** New User Created ({new_user.username}) **')
                    else:
                        print(f'** User Already Exists ({new_user.username}) **')

        except IOError:
            print(str(IOError))
            return