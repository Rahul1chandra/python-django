from django.db import models

# Create your models here.
class Event(models.Model):
    event_id = models.AutoField(primary_key= True)
    event_name  = models.CharField(max_length= 50)
    event_place  = models.CharField(max_length= 50)
    
    def __str__(self):
        return ("event name:  %s  and event place %s " % (self.event_name, self.event_place))


    ### we can use model manager class ###



class Personal(models.Model):
    name  =  models.CharField(max_length=122)



########## Django Models #####
#  get()       get we will use when we want to retrive object basaed on primary key
#  filter()    like a where clause in django orm  
#  __contains and __icontains  ex - object_list = Event.objects.filter(event_name__icontains="event_name") 
# include() and exculude ex  - vent.objects.filter(event_name__icontains="event_name").exclude(event_name__contains=' ')




