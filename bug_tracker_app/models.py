from django.db import models
from django.contrib.auth.models import User, AbstractUser


class BugTicket(models.Model):
    number = models.AutoField(primary_key=True)
    titles = models.CharField(max_length=60)
    assigned = models.CharField(max_length=30)
    reported = models.CharField(max_length=30)
    ticket_age = models.IntegerField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.number} - {self.titles}"


class BugSubmit(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()

    def __str__(self):
        return self.title

# class BugProfile(AbstractUser):
#    display_name = models.CharField(max_length = 30)

#     def __str__(self):
#         return self.display_name