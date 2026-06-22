from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        username = "Vamsic007"
        password = "Varshi@15"
        email = "vamsichallapalli01@gmail.com"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write("Default admin user created")
        else:
            self.stdout.write("Default admin user already exists")