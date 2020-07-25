from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views import View
from event.models import Event
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def index(request):   ### service  index 
    #return HttpResponse("my first page ....")
    if request.method == 'GET':
        return render(request,  'login.html', context={} )
    else:
        user_obj = authenticate(username= request.POST.get("username"), password=request.POST.get("password"))
        if user_obj.is_authenticated:
            login_obj = login(request, user_obj)
            return JsonResponse({"user_auth": True})
        else:
            return JsonResponse({"user_auth": False})

def logoutView(request):
    logout_auth = logout(request)
    return JsonResponse({"status": 201, "message": "user got logged out !"})


def signup(request):
    import ipdb; ipdb.set_trace()
    # https://docs.djangoproject.com/en/3.0/topics/auth/default/
    if request.method == 'POST':
        user_obj = User(username=request.POST.get('username'), 
                        email=request.POST.get('email'),
                        password=request.POST.get('password'))
        user_obj.save()
        return JsonResponse({})







class EventView(View):
   
    def get(self, request):  
        """GET method is used Getting the data from the database 
        """
        event_obj = Event.objects.all()
        response_list = []
        # import ipdb; ipdb.set_trace()
        for events in event_obj:
            response_list.append({"event_id": events.event_id, "event_name": events.event_name, "event_place": events.event_place })
        # print (response_list)
        return render(request,  'event_page.html', context={"event_list": response_list, "logged_in":request.user.get_username() } )
    
    
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
        elif request.POST.get('operation') == 'edit':
            # import ipdb; ipdb.set_trace()
            # print ("inside my edit ...")
            edit_obj = Event.objects.get(event_id = request.POST.get('event_id'))
            edit_obj.event_name = request.POST.get('event_name')
            edit_obj.event_place = request.POST.get('event_place')
            edit_obj.save()
            return JsonResponse({"create":True, "status_code": 201, "created_by": request.user.username })
  
        else:
            event = Event.objects.get(event_id= request.POST.get('event_id'))
            event.delete()
            return JsonResponse({"create":True, "status_code": 201, "created_by": request.user.username })