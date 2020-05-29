from django.urls import path
from bug_tracker_app import views

urlpatterns = [
    path("login/", views.loginview, name="loginpage"),
    path("logout/", views.logoutview),
    path("signup/", views.signupview),
    path("main/<int:id>/", views.submitview, name="homepage"),
    path("submission/", views.submissionadd, name="submissionpage")
]