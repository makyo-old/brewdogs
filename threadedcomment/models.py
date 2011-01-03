from django.db import models
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):
    topic_type = models.ForeignKey(ContentType)
    topic_id = models.IntegerField()
    parent = models.ForeignKey('Comment', null = True)
    owner = models.ForeignKey(User)
    title = models.CharField(max_length = 200)
    body = models.TextField()
