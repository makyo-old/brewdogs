from django.db import models
from django.contrib.auth.models import User
from brewdogs.brewsession.models import *

class UserProfile(models.Model):
    STATUS_CHOICES = (
            (0, "Lurker"),
            (1, "Brew pup"),
            (2, "Brew dog"),
            (3, "Master brew dog")
            )
    TYPE_CHOICES = (
            (0, "Brewer"),
            (1, "Mazer"),
            (2, "Vintner"),
            (3, "Distiller"),
            (4, "Consumer")
            )

    user = models.OneToOneField(User)
    bio = models.TextField(User, blank = True)
    location = models.CharField(max_length = 200, blank = True)
    date_of_birth = models.DateField()
    date_joined = models.DateTimeField(auto_now_add = True)
    member_status = models.IntegerField(choices = STATUS_CHOICES, default = 0)
    member_type = models.IntegerField(choices = TYPE_CHOICES, default = 4)
    fermentations_working = models.ManyToManyField(Fermentation, related_name = "users_working")
    distillations_working = models.ManyToManyField(Distillation, related_name = "users_working")
    fermentations_aging = models.ManyToManyField(Fermentation, related_name = "users_aging")
    distillations_aging = models.ManyToManyField(Distillation, related_name = "users_aging")
    fermentations_drinking = models.ManyToManyField(Fermentation, related_name = "users_drinking")
    distillations_drinking = models.ManyToManyField(Distillation, related_name = "users_drinking")
    recipes_docket = models.ManyToManyField(Recipe, related_name = "users_planning")
