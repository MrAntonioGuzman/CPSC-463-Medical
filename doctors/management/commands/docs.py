from django.core.management.base import BaseCommand, CommandError
from doctors.models import County, FakeDoctor


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_name = 'docs'
        l = []
        with open(file_name, 'r') as f:
            for line in f:
                l.append(line.strip())
            county = County.objects.get(county_name=l[0])
            doctor = FakeDoctor.objects.create(county=county, full_name=l[1], speciality=l[2], address=l[3],
                                               hospital=l[4])

