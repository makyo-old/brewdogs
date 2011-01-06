from brewdogs.brewsession.forms import *
from brewdogs.brewsession.models import *
from brewdogs.ajax_utils import *
from django.contrib.auth.decorators import login_required

@login_required
def add_fermentation_event(request):
    """
    Add an event to a fermentation
    """
    pass

def add_distillation_event(request):
    pass

def edit_fermentation_event(request):
    pass

def edit_distillation_event(request):
    pass

def delete_fermentation_event(request):
    pass

def delete_distillation_event(request):
    pass

def add_fermentation_to_working(request):
    pass

def add_distillation_to_working(request):
    pass

def add_fermentation_to_aging(request):
    pass

def add_distillation_to_aging(request):
    pass

def add_fermentation_to_drinking(request):
    pass

def add_distillation_to_drinking(request):
    pass

def remove_fermentation_from_lists(request):
    pass

def remove_distillation_from_lists(request):
    pass
