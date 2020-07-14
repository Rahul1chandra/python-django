from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):   ### service  index 
    #return HttpResponse("my first page ....")

    return render(request,  'login.html', context={} )

