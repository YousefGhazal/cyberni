from django.urls import path
from .views import (
    register_view,
    questions_view,
    callus_view,
    employer_view,
    result_view,
    aboutus_view,
)

urlpatterns = [
    path("", register_view, name="home"),
    path("questions/", questions_view, name="questions"),
    path("about-us/", aboutus_view, name="about-us"),
    path("result/", result_view, name="result"),
    path("call-us/", callus_view, name="call-us"),
    path("employer/", employer_view, name="employer"),
]
