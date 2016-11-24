from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from .forms import RegisterForm,LoginForm
from .models import User
# Create your views here.

def index(request):
    form = RegisterForm()
    context = {"registerForm":form}
    return render(request,"loginRegister/index.html",context)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        context = {"registerForm":form}
        if form.is_valid():
            newUser = User.objects.create(username=form.cleaned_data["username"],
                                          email=form.cleaned_data["email"],
                                          password=form.cleaned_data["password"])
            newUser.save()
            request.session["user"]=newUser.username
            return redirect(reverse("forum:index"))
        else:
            return render(request,"loginRegister/index.html",context)

def login(request):
    form = LoginForm()
    context = {"loginForm":form}
    return render(request,"loginRegister/login.html",context)

def authenticate(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        context = {"loginForm":form}
        if form.is_valid():
            request.session["user"]=form.cleaned_data["username"]
            return redirect(reverse("forum:index"))
        else:
            return render(request,"loginRegister/login.html",context)
