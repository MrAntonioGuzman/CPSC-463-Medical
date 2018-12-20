from django.core.management.base import BaseCommand, CommandError
from doctors.models import County


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_name = 'counties'
        with open(file_name, 'r') as f:
            for line in f:
                line = line.strip()
                county = County.objects.create(county_name=line)

