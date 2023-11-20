from django.db import models
from django.conf import settings


class Issue(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='issues')
    title = models.CharField(max_length=50)
    description = models.TextField()

    ISSUE_OPEN = 'OPEN'
    ISSUE_IN_PROGRESS = 'IN_PROGRESS'
    ISSUE_CLOSED = 'CLOSED'

    issue_status_choices = [
        (ISSUE_OPEN, 'Open'),
        (ISSUE_IN_PROGRESS, 'In Progress'),
        (ISSUE_CLOSED, 'Closed')
    ]

    status = models.CharField(
        max_length=11, choices=issue_status_choices, default=ISSUE_OPEN)

    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title}'
