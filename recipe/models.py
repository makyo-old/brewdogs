from brewdogs.choices import *
from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length = 250, blank = True)
    owner = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    category = models.ForeignKey('Category', null = True)
    equipment = models.ManyToManyField('EquipmentItem', null = True)
    batch_size = models.FloatField(max_digits = 5, decimal_places = 1, default = 5)
    batch_size_units = models.CharField(max_length = 4, choices = VOLUME_UNITS, default = 'gal')
    original_gravity = models.FloatField(max_digits = 4, decimal_places = 3, null = True)
    target_gravity = models.FloatField(max_digits = 4, decimal_places = 3, null = True)
    gravity_units = models.CharField(max_length = 2, choices = GRAVITY_CHOICES, blank = True)
    color = models.IntegerField(null = True)
    color_units = models.CharField(max_length = 3, choices = COLOR_CHOICES, blank = True)
    notes = models.TextField(blank = True)
    visible = models.BooleanField(default = False)

    def get_absolute_url(self):
        return "/recipe/%s/" % self.id

class Category(models.Model):
    slug = models.SlugField(primary_key = True)
    name = models.TextField(max_length = 200)
    description = models.TextField(blank = True)
    original_gravity_min = models.FloatField(max_digits = 4, decimal_places = 3, null = True)
    original_gravity_max = models.FloatField(max_digits = 4, decimal_places = 3, null = True)
    final_gravity_min = models.FloatField(max_digits = 4, decimal_places = 3, null = True)
    final_gravity_max = models.FloatField(max_digits = 4, decimal_places = 3, null = True)
    gravity_units = models.CharField(max_length = 2, choices = GRAVITY_CHOICES, blank = True)
    ibu = models.IntegerField(null = True)
    color = models.IntegerField(null = True)
    color_units = models.
    alcohol = models.FloatField(max_digits = 3, decimal_places = 1, null = True)
    alcohol_after_distillation = models.FloatField(max_digits = 3, decimal_places = 1, null = True)

    def get_absolute_url(self):
        return "/recipe/category/%s/" % self.slug

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe)
    item = models.ForeignKey('IngredientItem')
    amount = models.FloatField(max_digits = 6, decimal_places = 2)
    unit = models.CharField(max_length = 20)
    source = models.CharField(max_length = 250)

class IngredientItem(models.Model):
    UNIT_TYPES = (
            ('v', 'Volume'),
            ('w', 'Weight'),
            )
    category = models.ForeignKey('IngredientCategory')
    name = models.CharField(max_length = 200)
    brand = models.CharField(max_length = 200)
    color = models.IntegerField()
    gravity = models.FloatField(max_digits = 4, decimal_places = 3)
    unit_type = models.CharField(max_length = 1, choices = UNIT_TYPES)

class IngredientCategory(models.Model):
    name = models.CharField(max_length = 30)

class EquipmentItem(models.Model):
    usage = models.CharField(max_length = 50)
    name = models.CharField(max_length = 200)
    description = models.TextField()

class Step(models.Model):
    recipe = models.ForeignKey(Recipe)
    weight = models.IntegerField()
    text = models.TextField()
