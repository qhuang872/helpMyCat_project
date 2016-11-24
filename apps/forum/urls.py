from django.conf.urls import url
from . import views

app_name = "forum"

urlpatterns=[
        url(r"^$",views.index,name="index"),
        url(r"^logout",views.logout,name="logout"),
        url(r"^(?P<forumName>[a-zA-Z\s]+)/$",views.forum,name="forum"),
        url(r"^createThread$",views.createThread,name="createThread"),
        ]
