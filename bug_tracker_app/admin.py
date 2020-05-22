from django.contrib import admin
from bug_tracker_app.models import BugTicket, BugSubmit

admin.site.register(BugTicket),
admin.site.register(BugSubmit)
