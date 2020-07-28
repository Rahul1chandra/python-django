from django.conf import settings 
import smtplib 

##  twilio
# Go to this link and select Turn On
# https://www.google.com/settings/security/lesssecureapps

def mailnotification(message, receiver_mailid):
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login(settings.SMTP_USERNAME, settings.ACCOUNT_PASSWORD) 
        s.sendmail(settings.SMTP_USERNAME, receiver_mailid, message) 
        s.quit()
        print ("Message Sent Successfully")
    except Exception as er:
        print ("error in sending messages ")
    


## i created my gmail account 
## 


def smsnotification():
    pass