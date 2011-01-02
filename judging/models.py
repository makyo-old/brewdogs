from django.db import models
from django.contrib.auth.models import User

class ScoreCard50(models.Model):
    TYPE_CHOICES = (
            ("Fermentation", "Beer, wine, mead, or other fermented beverage"),
            ("Distillation", "Whiskey, brandy, vodka, or other distilled beverage")
            )

    subject_type = models.CharField(max_length = 15, choices = TYPE_CHOICES)
    subject_id = models.IntegerField()
    reviewer = models.ForeignKey(User)
    aroma_malt = models.IntegerField(verbose_name = "Aroma - malt")
    aroma_hops = models.IntegerField(verbose_name = "Aroma - hops")
    aroma_other = models.IntegerField(verbose_name = "Aroma - other fermentation characteristics")
    appearance_color = models.IntegerField(verbose_name = "Appearance - color")
    appearance_clarity = models.IntegerField(verbose_name = "Appearance - clarity")
    appearance_head = models.IntegerField(verbose_name = "Appearance - head retention")
    flavor_malt = models.IntegerField(verbose_name = "Flavor - malt")
    flavor_hops = models.IntegerField(verbose_name = "Flavor - hops")
    flavor_balance = models.IntegerField(verbose_name = "Flavor - balance")
    flavor_conditioning = models.IntegerField(verbose_name = "Flavor - conditioning and carbonation")
    flavor_aftertaste = models.IntegerField(verbose_name = "Flavor - aftertaste")
    body = models.IntegerField()
    overall_drinkability = models.IntegerField(verbose_name = "Overall impressions and drinkability")
    notes_aroma = models.TextField(blank = True, verbose_name = "Aroma - notes")
    notes_appearance = models.TextField(blank = True, verbose_name = "Appearance - notes")
    notes_flavor = models.TextField(blank = True, verbose_name = "Flavor - notes")
    notes_body = models.IntegerField(blank = True, verbose_name = "Body - notes")
    notes_overall = models.IntegerField(blank = True, verbose_name = "Overall notes")

    def aroma(self):
        return self.aroma_malt + self.aroma_hops + self.aroma_other

    def appearance(self):
        return self.appearance_color + self.appearance_clarity + self.appearance_head

    def flavor(self):
        return self.flavor_malt + self.flavor_hops + self.flavor_balance + self.flavor_conditioning + self.flavor_aftertaste

    def total(self):
        return self.aroma() + self.appearance() + self.flavor() + self.body + self.overal_drinkability

class ScoreCard20(models.Model):
    TYPE_CHOICES = (
            ("Fermentation", "Beer, wine, mead, or other fermented beverage"),
            ("Distillation", "Whiskey, brandy, vodka, or other distilled beverage")
            )

    subject_type = models.CharField(max_length = 15, choices = TYPE_CHOICES)
    subject_id = models.IntegerField()
    reviewer = models.ForeignKey(User)
    appearance = models.IntegerField()
    aroma = models.IntegerField()
    taste_balance = models.IntegerField()
    taste_aftertaste = models.IntegerField()
    taste_mouthfeel = models.IntegerField()
    overall = models.IntegerField()
    notes_appearance = models.TextField(blank = True)
    notes_aroma = models.TextField(blank = True)
    notes_taste = models.TextField(blank = True)
    notes_overall = models.TextField(blank = True)

    def taste(self):
        return self.taste_balance + self.taste_aftertaste + self.taste_mouthfeel

    def total(self):
        return self.taste() + self.appearance + self.aroma + self.overall
