from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    likes = models.IntegerField(0, default=0)
    posted = models.DateField(default=datetime.now)

    class Meta:
        ordering = ('-posted',)

        def __str__(self):
            return self.subject

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE )
    comment = models.TextField()
    likes = models.IntegerField(0, default=0)
    posted = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ('-posted',)

        def __str__(self):
            return self.comment

