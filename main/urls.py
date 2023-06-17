from django.urls import path
from .views import (
    index_view,
    dashboard_view,
    register_view,
    questions_view,
    callus_view,
    employer_view,
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", index_view, name="home"),
    path("questions/", questions_view, name="questions"),
    path("call-us/", callus_view, name="call-us"),
    path("employer/", employer_view, name="employer"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("register/", register_view, name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
]
