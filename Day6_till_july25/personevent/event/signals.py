from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from event.notifications import mailnotification




@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):      ## callback API/function 
    ### we can write our business logic
    mailnotification(message="Profile created enjoy with us", receiver_mailid=instance.email)
    print ("execution complated ..........!!")