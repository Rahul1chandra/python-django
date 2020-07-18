from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views import View
from event.models import Event

def index(request):   ### service  index 
    #return HttpResponse("my first page ....")

    return render(request,  'login.html', context={} )




class EventView(View):
   
    def get(self, request):  
        """GET method is used Getting the data from the database 
        """
        event_obj = Event.objects.all()
        response_list = []
        for events in event_obj:
            response_list.append({"event_id": events.event_id, "event_name": events.event_name, "event_place": events.event_place })
        # print (response_list)
        return render(request,  'event_page.html', context={"event_list": response_list} )
    
    
    def post(self, request):
        """POST method is used from pushing the data to the database 
          adding the new data to the database 
        """
        # import ipdb; ipdb.set_trace()  # lib used for debugging ....
        if request.POST.get('operation') == 'add':
            event_name = request.POST.get('event_name')
            event_place = request.POST.get('event_place')
            event_obj = Event(event_name= event_name, event_place= event_place)
            event_obj.save()
            return JsonResponse({"create":True, "status_code": 200, "created_by": request.user.username })
        else:
            event = Event.objects.get(event_id= request.POST.get('event_id'))
            event.delete()
            return JsonResponse({"create":True, "status_code": 201, "created_by": request.user.username })