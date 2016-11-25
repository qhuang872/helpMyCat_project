from django.conf.urls import url
from . import views

app_name = "forum"

urlpatterns = [
        url(r"^$",views.index,name="index"),
        url(r"^logout",views.logout,name="logout"),
        url(r"^(?P<forumName>.+)/$",views.forum,name="forum"),
        url(r"^newThread$",views.newThread,name="newThread"),
        url(r"^createThread$",views.createThread,name="createThread"),
        url(r"^thread/(?P<thread>.+)",views.showThread,name="showThread"),
        url(r"^post$",views.newPost,name="newPost"),
        url(r"^createForum",views.newForum,name="newForum"),
        
        ]
