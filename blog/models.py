from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# each class will be the own table for the database.
# each attribute will the field of the database.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # using django time-frame
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    # CASCADE tells when user is deleted, his post will be deleted.

    def __str__(self):
        return self.title