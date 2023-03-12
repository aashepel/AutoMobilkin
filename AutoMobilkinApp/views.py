from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import date

from AutoMobilkinApp.models import Car
from django.db import connection


# Create your views here.

def hello(request):
    return render(request, 'index.html', {
        'current_date': date.today()
    })


def index(request):
    return HttpResponseRedirect("/cars")


def cars(request):
    count_on_page = request.GET.get('count_on_page')
    page = request.GET.get('page')

    if page is None:
        page = 0

    if count_on_page is None:
        count_on_page = 10

    cars_list = Car.objects.all()[int(page)*int(count_on_page):int(page)*int(count_on_page)+int(count_on_page)]
    return render(request, 'cars.html', {'cars_list': cars_list, 'count_on_page': count_on_page, 'page': page})


def get_car(request, id):
    car_info = Car.objects.get(id=id)
    return render(request, 'car_info.html', {'car_info': car_info})

def delete_confirm_delete_view(request, id):
    car_info = Car.objects.get(id=id)
    return render(request, 'car_confirm_delete.html', {'car_info': car_info})

def delete_car(request, id):
    # delete an object and send a confirmation response
    cursor = connection.cursor()
    cursor.execute('DELETE FROM "public"."AutoMobilkinApp_car" WHERE id = %s', [id])
    return HttpResponseRedirect("/cars")
