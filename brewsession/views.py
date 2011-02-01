from brewdogs.brewsession.models import *
from brewdogs.brewsession.forms import *
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.templates import RequestContext
from django.contrib.auth.decorators import login_required

def show_fermentation(request, id):
    """
    Show a fermentation
    """
    fermentation = get_object_or_404(Fermentation, id = id)
    return render_to_response("brewsession/fermentation/show.html", context_instance = RequestContext(request, {'fermentation': fermentation}))

def show_distillation(request, id):
    """
    Show a distillation
    """
    distillation = get_object_or_404(Distillation, id = id)
    return render_to_response("brewsession/distillation/show.html", context_instance = RequestContext(request, {'distillation': distillation}))

@login_required
def edit_fermentation(request, id):
    """
    Edit a fermentation
    """
    fermentation = get_object_or_404(Fermentation, id = id)
    if request.user == fermentation.brewmaster or request.user.is_staff():
        form = FermentationForm(instance = fermentation)
        if request.method == "POST":
            form = FermentationForm(request.POST, instance = fermentation)
            if form.is_valid():
                fermentation = form.save()
                request.user.message_set.create('<div class="success">Fermentation saved</div>')
                return redirect(fermentation)
        return render_to_response("brewsession/fermentation/edit.html", context_instance = RequestContext(request, {'form': form, 'fermentation': fermentation}))
    else:
        return render_to_response("errors/403.html", context_instance = RequestContext(request, {}))


def edit_distillation(request, id):
    """
    Edit a distillation
    """
    distillation = get_object_or_404(Distillation, id = id)
    if request.user == distillation.brewmaster or request.user.is_staff():
        form = DistillationForm(instance = distillation)
        if request.method == "POST":
            form = DistillationForm(request.POST, instance = distillation)
            if form.is_valid():
                distillation = form.save()
                request.user.message_set.create('<div class="success">Distillation saved</div>')
                return redirect(distillation)
        return render_to_response("brewsession/distillation/edit.html", context_instance = RequestContext(request, {'form': form, 'distillation': distillation}))
    else:
        return render_to_response("errors/403.html", context_instance = RequestContext(request, {}))

def delete_fermentation(request, id):
    """
    Delete a fermentation
    """
    fermentation = get_object_or_404(Fermentation, id = id)
    if request.user == fermentation.brewmaster or request.user.is_staff():
        

def delete_distillation(request, id):
    pass

def create_fermentation(request, recipe_id):
    pass

def create_distillation(request, fermentation_id):
    pass

