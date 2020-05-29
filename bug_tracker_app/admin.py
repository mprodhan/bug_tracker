from django.contrib import admin
from bug_tracker_app.models import BugTicket, BugProfile
from django.contrib.auth.admin import UserAdmin

admin.site.register(BugTicket),
admin.site.register(BugProfile, UserAdmin)
