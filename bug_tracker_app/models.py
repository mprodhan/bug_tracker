from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone
from bug_tracker.settings import AUTH_USER_MODEL


class BugTicket(models.Model):
    title = models.CharField(max_length=60, default=None)
    date_filed = models.DateTimeField(default=timezone.now)
    description = models.TextField(default=None)
    # The person who filed the ticket
    reporter_name = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="reporter_name", default=None)
    NEW = "n"
    IN_PROGRESS = "ip"
    DONE = "d"
    INVALID = "inv"
    STATUS_OF_TICKET = [
        (NEW, "n"),
        (IN_PROGRESS, "ip"),
        (DONE, "d"),
        (INVALID, "inv")
    ]

    status_of_ticket = models.CharField(max_length=5,
        choices=STATUS_OF_TICKET, default=NEW
    )

    ticket_assigned = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="ticket_assigned", default=None, null=True, blank=True)

    ticket_completed = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="ticket_completed", default=None, null=True, blank=True)

    def __str__(self):
        return self.title

class BugProfile(AbstractUser):
    display_name = models.CharField(max_length=30)

    def __str__(self):
        return self.display_name