from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from .models import Forum, Thread, Post

# Create your views here.
def index(request):
    allForum = Forum.objects.all()
    context={"all":allForum}
    return render(request,"forum/index.html",context)

def logout(request):
    request.session.remove("user")
    return redirect(reverse("index:index"))

def forum(request,forumName):
    context = {"forum":forumName}
    return render(request,"forum/forum.html",context)

def createThread(request):
    return render(request,"forum/newThread.html")

