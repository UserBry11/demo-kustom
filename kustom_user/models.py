from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class MyKustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Ticket(models.Model):
    Status_Choices = [
        ('New', 'New'),
        ('In-Progress', 'In-Progress'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid')
    ]

    title = models.CharField(max_length=30, default="Default text here")
    date_filed = models.DateTimeField(default=timezone.now)
    description = models.TextField(default="Default body here")
    user_who_filed = models.ForeignKey(MyKustomUser,
                                       on_delete=models.CASCADE,
                                       null=True,
                                       blank=True,
                                       related_name="user_who_filed")
    status_of_ticket = models.CharField(max_length=11,
                                        blank=True,
                                        choices=Status_Choices)
    user_assigned_to = models.ForeignKey(MyKustomUser,
                                         on_delete=models.CASCADE,
                                         null=True,
                                         blank=True,
                                         related_name="user_assigned_to")
    user_who_completed = models.ForeignKey(MyKustomUser,
                                           on_delete=models.CASCADE,
                                           null=True,
                                           blank=True,
                                           related_name="user_who_completed")
