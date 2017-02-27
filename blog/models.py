from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    """
    Here we'll define our Post model
    """

    # author is linked to a registered
    # user in the 'auth_user' table
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def pushlish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title
