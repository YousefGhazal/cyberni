from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


def index_view(request):
    return render(request, "about-us.html")


@login_required()
def dashboard_view(request):
    return render(request, "home.html")


def register_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.object.get()
            return redirect("home")
    else:
        form = UserForm()
    return render(request, "login.html", {"form": form})
