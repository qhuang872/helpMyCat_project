from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from .models import Forum, Thread, Post
from ..loginRegister.models import User
# Create your views here.
def index(request):
    allForum = Forum.objects.all()
    health = Forum.objects.get(forum="Cat Health")
    nutrition = Forum.objects.get(forum="Cat Nutrition")
    behavior = Forum.objects.get(forum="Cat Behavior")
    care = Forum.objects.get(forum="Cat Care & Grooming")
    new = Forum.objects.get(forum="New Cat")
    pregnant = Forum.objects.get(forum="Pregnant Cats and Kitten Care")
    dog = Forum.objects.get(forum="Cats and Dogs")
    context={"allForum":allForum,
            "health":health,
            "nutrition":nutrition,
            "behavior":behavior,
            "care":care,
            "new":new,
            "pregnant":pregnant,
            "dog":dog,
            }
    return render(request,"forum/index.html",context)

def logout(request):
    request.session.pop("user")
    return redirect(reverse("loginRegister:index"))

def forum(request,forumName):
    currentForum = Forum.objects.get(forum=forumName)
    allThread = currentForum.thread_set.all()
    context = {"allThread":allThread}
    request.session["forum"] = forumName;
    return render(request,"forum/forum.html",context)

def newThread(request):
    currentForum = request.session["forum"]
    context = {"forum":currentForum}
    return render(request,"forum/newThread.html",context)

def createThread(request):
    if request.method=="POST":
        threadTitle = request.POST["thread"]
        creator = User.objects.get(username=request.session["user"])
        currentForum = Forum.objects.get(forum=request.session["forum"])
        newThread = Thread.objects.create(thread=threadTitle,forum=currentForum,creator=creator)
        newThread.save();
        currentForum.thread_set.add(newThread)
        currentForum.save()
        optionalPost = request.POST["post"]
        if optionalPost != "":
            newPost = Post.objects.create(post=optionalPost,thread=newThread,writer=creator)
            newThread.post_set.add(newPost)
            newThread.save()
        return redirect(reverse("forum:forum",kwargs={"forumName":request.session["forum"]})) 
            
def showThread(request,thread):
    thread = Thread.objects.get(thread=thread)
    allPost = thread.post_set.all()
    context = {"allPost":allPost,"currentThread":thread}
    return render(request,"forum/showThread.html",context)

def newPost(request):
    if request.method == "POST":
        post = request.POST["post"]
        writer = User.objects.get(username=request.session["user"])
        currentThread = request.POST["currentThread"]
        thread = Thread.objects.get(thread=currentThread)
        newPost = Post.objects.create(post=post,thread=thread,writer=writer)
        newPost.save()
        thread.post_set.add(newPost)
        thread.save()
        return redirect(reverse("forum:showThread",kwargs={"thread":currentThread}))

def newForum(request):
    if request.method == "POST":
        forumTitle = request.POST["forumTitle"]
        description = request.POST["description"]
        newForum = Forum.objects.create(forum=forumTitle,description=description)
        newForum.save()
        return redirect(reverse("forum:index"))

