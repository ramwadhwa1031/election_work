from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.
from data.models import Post


def user_login(request):
    queryset= Post.objects.all()
    context={
        "objects_list" : queryset
       }

    if request.method == 'POST':
        phone = request.POST['phoneno']

        #password = request.POST['password']
        user = authenticate(request, phone=phone)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In!"))
            # Redirect to a success page.
            return redirect('/success/')
        else:
            messages.success(request, ("Error Loggin In - Please Try Again..."))
            # Return an 'invalid login' error message.
            return redirect('/login/')
    else:
        return render(request, "registration.html", {})



def user_logout(request):
    pass

def success(request):
    pass

#def createpost(request):
#        if request.method == 'POST':
#            if request.POST.get('phone'):
#                post=Post()
#                post.phone= request.POST.get('phone')

#                post.save()
#
#                return render(request, 'posts/registration.html')
#
#        else:
#                return render(request,'posts/registration.html')
