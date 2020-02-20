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

    title = models.CharField(max_length=30)
    date_filed = models.DateTimeField(default=timezone.now)
    description = models.TextField()
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



"""
Title
Time/Date filed
Description
Name of user who filed ticket
Status of ticket (New / In Progress / Done / Invalid)
Name of user assigned to ticket
Name of user who completed ticket


When a ticket is created, it should have the following settings:

Status: New
User Assigned: None
User who Completed: None
User who filed: Person who's logged in
When a ticket is assigned, these change as follows:

Status: In Progress
User Assigned: person the ticket now belongs to
User who Completed: None
When a ticket is Done, these change as follows:

Status: Done
User Assigned: None
User who Completed: person who the ticket used to belong to
When a ticket is marked as Invalid, these change as follows:

 Status: Invalid
User Assigned: None
User who Completed: None
"""