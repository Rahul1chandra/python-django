from django.urls import path

from event.views import index, EventView, logoutView, signup, dashboard, viewtest


urlpatterns = [
    path('', index, name='index'),
    path('eventpage/', EventView.as_view()),  ### best proximity
    path('logout/', logoutView, name='logout'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),

    path('viewtest/', viewtest, name='viewtest')
    
    ]