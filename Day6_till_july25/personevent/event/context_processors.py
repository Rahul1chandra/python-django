from django.conf import settings

def gloablvariable(request):
    import ipdb; ipdb.set_trace();
    if request.path not in ['/admin/', '/']:
        return {"user": request.user.username, "last_login": request.user.last_login.__str__()}
    else:
        return {}