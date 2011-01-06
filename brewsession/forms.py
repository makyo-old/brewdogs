from brewdogs.brewsession.models import *
from django.forms import ModelForm

class FermentationForm(ModelForm):
    class Meta:
        model = Fermentation

class DistillationForm(ModelForm):
    class Meta:
        model = Distillation

class FermentationEventForm(ModelForm):
    class Meta:
        model = FermentationEvent

class DistillationEventForm(ModelForm):
    class Meta:
        model = DistillationEvent


