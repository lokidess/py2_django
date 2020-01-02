from django.db import models


class Todo(models.Model):

    PRIORITY_CHOICES = (
        (1, 'Max'),
        (2, 'Not so max'),
        (3, 'Medium'),
        (4, 'So so'),
        (5, 'Low')
    )

    text = models.TextField()
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.text
