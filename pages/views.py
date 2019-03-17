from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def user_login(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "registration.html", {})


def home_view(request, *args, **kwargs):

    return render(request, "home.html", {})

def login_view(request, *args, **kwargs):

    return render(request, "login.html", {})
