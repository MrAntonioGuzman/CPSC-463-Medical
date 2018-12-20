from django.shortcuts import render
from .models import County, FakeDoctor
from django.core import serializers
from django.http import JsonResponse


def doctors(request):
    counties = County.objects.all()
    return render(request, 'doctors/doctors.html', {'counties': counties})


def ajax_search(request):
    if request.is_ajax():
        selected = request.GET.get('selected', None)
        print(selected)
        try:
            doctors = FakeDoctor.objects.get(county__county_name=selected)
            data = serializers.serialize('json', [doctors])
        except FakeDoctor.DoesNotExist:
            data = False
    else:
        data = 'fail'
    return JsonResponse(data, safe=False)
