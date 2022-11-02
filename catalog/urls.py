from django.urls import path

from .views import person, triangle, update_person


app_name = 'catalog'
urlpatterns = [
    path('', triangle, name='triangle'),
    path('person', person, name='person'),
    path('person/<int:pk>', update_person, name='update_person')
]
