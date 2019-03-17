from django.shortcuts import render

# Create your views here.


def login_page(request):
    form =LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path =next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path,request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            print("Error")
        return render(request, "login.html",context)

User=get_user_model()

def register_page(request):
    form=RegisterForm(request.POST or None)
    context ={
        "form" : form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username= form.cleaned_data.get("username")
        phone= form.cleaned_data.get("phone")
        password= form.cleaned_data.get("password")
        new_user = User.objects.create_user(username)
