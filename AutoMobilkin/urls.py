from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from AutoMobilkin import settings
from AutoMobilkinApp import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('cars/', views.cars),
    path('cars/', views.cars),
    path('cars/<int:id>/', views.get_car)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
