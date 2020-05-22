from django import forms
from bug_tracker_app.models import BugTicket

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50)
    password = forms.CharField(widget = forms.PasswordInput)