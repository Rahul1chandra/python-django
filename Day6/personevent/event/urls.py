from django.urls import path

from event.views import index, EventView


urlpatterns = [
    path('', index, name='index'),
    path('eventpage/', EventView.as_view())  ### best proximity 
    ]