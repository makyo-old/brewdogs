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
    recipe = models.ForeignKey(Recipe)
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
    EVENT_TYPES = (
            (0, "Mash-in"),
            (1, "Mash note"),
            (2, "Mash-out"),
            (3, "Lauter"),
            (4, "Sparge"),
            (5, "Boil start"),
            (6, "Boil note"),
            (7, "Bittering hops"),
            (8, "Flavor hops"),
            (9, "Aroma hops"),
            (10, "Dry hops"),
            (11, "Cool start"),
            (12, "Cool note"),
            (13, "Cool end"),
            (14, "Yeast pitched"),
            (15, "Fermentation start"),
            (16, "Fermentation note"),
            (17, "Rack to secondary"),
            (18, "Lagering"),
            (19, "Fermentation end"),
            (20, "Backsweeten"),
            (21, "Other ingredient addition"),
            (22, "Hydrometer reading"),
            (23, "Bottling"),
            (24, "Bottling note"),
            (25, "Bottle conditioning"),
            (26, "Aging"),
            (27, "Sampling"),
            (28, "Last of batch consumed"),
            (29, "General note")
            )

    event_type = models.IntegerField(choices = EVENT_TYPES)
    event_datetime = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User)
    notes = models.TextField(blank = True)

class DistillationEvent(models.Model):
    EVENT_TYPES = (
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
            )

    event_type = models.IntegerField(choices = EVENT_TYPES)
    event_datetime = models.DateTimeEvent(auto_now_add = True)
    owner = models.ForeignKey(User)
    notes = models.TextField(blank = True)
