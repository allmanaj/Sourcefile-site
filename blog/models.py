import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_body = models.TextField()
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.post_title

    def was_publised_recently(self):
        return self.pud_date >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_body = models.TextField()
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.comment_body
