from django.urls import path
from bug_tracker_app import views

urlpatterns = [
    path("login/", views.loginview, name="loginpage"),
    path("logout/", views.logoutview),
    path("signup/", views.signupview),
    path("submit/", views.submissionadd, name="submitpage")
]