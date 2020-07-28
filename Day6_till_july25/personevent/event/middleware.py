from django.utils.deprecation import MiddlewareMixin

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect

EXEMPT_URLS = ['/', '/signup/', "/admin/"]
class LoginRequiredMiddleware(MiddlewareMixin):
    
    def process_request(self, request):  
        ### user logger 
        ## Step 1 :get the username and requested path ,
        ## step 2 :keep/write it in some file txt
        ## step 3 : capture the request path , the user 
        ## step 4: with the help of file cvs, txt we can do some analystics ..
        # import ipdb; ipdb.set_trace()    ### debugger tool
        if not request.user.is_authenticated:
            if request.path not in EXEMPT_URLS:
                return HttpResponseRedirect("/")