from django.db import models

class Comment(models.Model):
    topic_type = models.CharField(max_length = 50)
    topic_id = models.IntegerField()
    parent = models.ForeignKey('Comment', null = True)
    owner = models.ForeignKey(User)
    title = models.CharField(max_length = 200)
    body = models.TextField()
