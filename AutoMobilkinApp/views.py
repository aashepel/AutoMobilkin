from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import date

from AutoMobilkinApp.models import Car


# Create your views here.

def hello(request):
    return render(request, 'index.html', {
        'current_date': date.today()
    })


def index(request):
    return HttpResponseRedirect("/cars")


def cars(request):
    count_on_page = request.GET.get('count_on_page')
    if count_on_page is None:
        cars_list = Car.objects.all()
    else:
        cars_list = Car.objects.all()[:int(count_on_page)]
    return render(request, 'cars.html', {'cars_list': cars_list, 'count_on_page': count_on_page})


def get_car(request, id):
    car_info = Car.objects.get(id=id)
    return render(request, 'car_info.html', {'car_info': car_info})
