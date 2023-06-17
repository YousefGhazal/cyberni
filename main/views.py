from django.shortcuts import render, redirect
from .forms import UserForm
import random
from .models import Cert


# Create your views here.


def register_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("result")
    else:
        form = UserForm()
    return render(request, "login.html", {"form": form})

def result_view(request):
    certs = Cert.objects.all()
    cert_one = random.choice(certs)
    cert_two = random.choice(certs)

    return render(request, "result.html", {"cert_one":cert_one, "cert_two":cert_two})


def callus_view(request):
    return render(request, "call-us.html")


def aboutus_view(request):
    return render(request, "about-us.html")


def employer_view(request):
    return render(request, "employer.html")


def questions_view(request):
    return render(request, "questions.html")

