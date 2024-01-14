from django.core.management.base import BaseCommand
from details.models import Draws


class LoadDrw(BaseCommand):
    help = "Load all draws to bd"

    def load_img_list(path=""):
        images = []
        return images

    def handle(self, *args, **kwargs):
        self.stdout.write("loading images... \n")
        draws = self.load_img_list()
        for drw in draws:
            Draws.objects.get_or_create(name="drw")
            self.stdout.write(f'loading {drw}...')
            