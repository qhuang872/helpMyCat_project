from django.conf.urls import url
from . import views


app_name="loginRegister"

urlpatterns=[
        url(r"^$",views.index,name="index"),
        url(r"^register$",views.register,name="register"),
        url(r"^login$",views.login,name="login"),
        url(r"^authenticate$",views.authenticate,name="authenticate"),
        ]
