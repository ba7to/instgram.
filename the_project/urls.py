from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
urlpatterns = [
    path("",views.instgram),
    path("phones/",views.Home),
    path("register/",views.register),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]