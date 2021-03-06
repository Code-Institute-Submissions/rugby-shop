from django.db import models
from django.utils import timezone

# Create your models here.

"""
The Review model
"""


class Review(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    added_by = models.CharField(max_length=20, default='Emma')

    def __unicode__(self):
        return self.title
