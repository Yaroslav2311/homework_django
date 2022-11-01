from django.urls import path

from .views import triangle

app_name = 'catalog'
urlpatterns = [
    path('', triangle, name='triangle'),

]
