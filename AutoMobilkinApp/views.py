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
    cars_list = Car.objects.all()
    return render(request, 'cars.html', {'cars_list': cars_list})


def get_car(request, id):
    car_info = Car.objects.get(id=id)
    return render(request, 'car_info.html', {'car_info': car_info})
