from django import forms
from bug_tracker_app.models import BugTicket

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class Registration(forms.Form):
    name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    display_name = forms.CharField(max_length=30)

class TicketSubmission(forms.Form):
    title = forms.CharField(max_length=60)
    description = forms.CharField(widget=forms.TextInput)