from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from bug_tracker_app.forms import LoginForm, Registration
from bug_tracker_app.models import BugTicket

def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data["username"],
                password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage"))
                )
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse("loginpage"))

def signupview(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = BugTicket.objects.create_user(
                name = data["name"],
                username = data["name"],
                password = data["password"],
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
    form = Registration()
    return render(request, "generic_form.html", {"form": form})