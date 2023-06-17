from django.urls import path
from .views import index_view, dashboard_view, register_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", index_view, name="home"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", register_view, name="register"),
    path("logout/", LogoutView.as_view(next_page="dashboard"), name="logout"),
]
