from django.db import models
from brewdogs.recipe.models import *
from django.contrib.auth.models import User

class Fermentation(models.Model):
    recipe = models.ForeignKey(Recipe)
    brewmaster = models.ForeignKey(User, related_name = 'fermentations_master_of')
    participants = models.ManyToManyField(User, related_name = 'fermentations_participated_in', blank = True, null = True)
    notes = models.TextField(blank = True)
    batch_size = models.FloatField(max_digits = 5, decimal_places = 1)

class Distillation(models.Model):
    recipe = models.ForeignKey(Fermentation)
    brewmaster = models.ForeignKey(User, related_name = 'distillations_master_of')
    participants = models.ManyToManyField(User, related_name = 'distillations_participated_in', blank = True, null = True)
    notes = models.TextField(blank = True)
    is_strip_run = models.BooleanField(default = False)
    keep_yield = models.FloatField(max_digits = 5, decimal_places = 2)
    feints_yield = models.FloatField(max_digits = 5, decimal_places = 2, null = True)
    start_cut_temp = models.FloatField(max_digits = 4, decimal_places = 1, null = True)
    start_cut_abv = models.FloatField(max_digits = 3, decimal_places = 1, null = True)
    end_cut_temp = models.FloatField(max_digits = 4, decimal_places = 1, null = True)
    end_cut_abv = models.FloatField(max_digits = 3, decimal_places = 1, null = True)

class FermentationEvent(models.Model):
    """
            (0, "Dough in"),
            (1, "Mash-in"),
            (2, "Mash note"),
            (3, "Mash-out"),
            (4, "Lauter"),
            (5, "Sparge"),
            (6, "Steep"),
            (6, "Boil start"),
            (7, "Boil note"),
            (8, "Bittering hops"),
            (9, "Flavor hops"),
            (10, "Aroma hops"),
            (11, "Dry hops"),
            (12, "Cool start"),
            (13, "Cool note"),
            (14, "Cool end"),
            (15, "Yeast pitched"),
            (16, "Fermentation start"),
            (17, "Fermentation note"),
            (18, "Rack to secondary"),
            (19, "Lagering"),
            (20, "Fermentation end"),
            (21, "Backsweeten"),
            (22, "Other ingredient addition"),
            (23, "Hydrometer reading"),
            (24, "Bottling"),
            (25, "Bottling note"),
            (26, "Bottle conditioning"),
            (27, "Aging"),
            (28, "Sampling"),
            (29, "Last of batch consumed"),
            (30, "General note")
    """

    event = models.ForeignKey('Event')
    fermentation = models.ForeignKey(Fermentation)
    event_datetime = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User)
    notes = models.TextField(blank = True)

class DistillationEvent(models.Model):
    """
            (0, "Boil start"),
            (1, "Foreshots"),
            (2, "Start collecting"),
            (3, "Heads note")
            (4, "Start cut"),
            (5, "Hearts note"),
            (6, "End cut"),
            (7, "Tails note"),
            (8, "Stop collecting"),
            (9, "Collection note"),
            (10, "Start airing"),
            (11, "Airing note"),
            (12, "End airing"),
            (13, "Start oaking"),
            (14, "Oaking note"),
            (15, "End oaking"),
            (16, "Start maceration"),
            (17, "Maceration note"),
            (18, "End maceration"),
            (19, "Alcoholmeter reading"),
            (20, "Dilution")
            (21, "Aging"),
            (22, "Sampling"),
            (23, "Last of batch consumed"),
            (24, "General note")
    """

    event = models.ForeignKey('Event')
    distillation = models.ForeignKey(Distillation)
    event_datetime = models.DateTimeEvent(auto_now_add = True)
    owner = models.ForeignKey(User)
    notes = models.TextField(blank = True)

class Event(models.Model):
    TYPE_CHOICES = (
            ("F", "Fermentation"),
            ("D", "Distillation")
            )

    event_type = models.CharField(max_length = 1, choices = TYPE_CHOICES)
    event_text = models.CharField(max_length = 50)
