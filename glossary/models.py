from django.db import models

class Term(models.Model):
    term = models.CharField(max_length = 100)
    definition = models.TextField()
