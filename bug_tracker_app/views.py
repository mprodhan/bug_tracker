from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from bug_tracker_app.forms import LoginForm, Registration, TicketSubmission
from bug_tracker_app.models import BugTicket, BugProfile

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
                return HttpResponseRedirect(reverse("submissionpage")
                )
    form = LoginForm()
    return render(request, "loginpage.html", {"form": form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse("loginpage"))

def signupview(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = Registration.objects.create_user(
                name = data["name"],
                username = data["username"],
                password = data["password"],
                display_name = data["display_name"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("loginpage"))
    form = Registration()
    return render(request, "signup.html", {"form": form})

@login_required
def submissionadd(request):
    if request.method =="POST":
        form = TicketSubmission(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = BugTicket.objects.create(
                title = data["title"],
                description = data["description"]
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = TicketSubmission()
    return render(request, "generic_form.html", {"form": form})

@login_required
def submitview(request, id):
    ticket = BugTicket.objects.all()
    return render(request, "main.html", {"ticket": ticket})