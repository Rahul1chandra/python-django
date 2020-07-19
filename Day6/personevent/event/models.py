from django.db import models

# Create your models here.
class Event(models.Model):
    event_id = models.AutoField(primary_key= True)
    event_name  = models.CharField(max_length= 50)
    event_place  = models.CharField(max_length= 50)
    
    def __str__(self):
        return ("event name:  %s  and event place %s " % (self.event_name, self.event_place))


class Personal(models.Model):
    name  =  models.CharField(max_length=122)