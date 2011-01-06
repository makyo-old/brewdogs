from brewdogs.recipe.forms import *
from brewdogs.recipe.models import *
from brewdogs.ajax_utils import *

@login_required
def add_ingredient(request):
    """
    Add an ingredient to a recipe
    """
    if request.method = "POST" and request.is_ajax():
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return _respond('success')
    else:
        return _respond('failure')

@login_required
def add_equipment_item(request):
    """
    Add an equipment item to a recipe
    """
    if request.method == "POST" and request.is_ajax():
        if request.POST.get('equipment_item_id', None) is not None and request.POST.get('recipe_id', None) is not None:
            recipe = Recipe.objects.get(id = request.POST['recipe_id'])
            equipment_item = EquipmentItem.objects.get(id = request.POST['equipment_item_id'])
            recipe.equipment_set.add(equipment_item)
            recipe.save()
            return _respond('success')
    else:
        return _respond('failure')

@login_required
def add_step(request):
    """
    Add a step to a recipe
    """
    if request.method == "POST" and request.is_ajax():
        form = StepForm(request.POST)
        if form.is_valid():
            form.save()
            return _respond('success')
    else:
        return _respond('failure')

@login_required
def edit_ingredient(request):
    """
    Edit an ingredient in a recipe
    """
    if request.method = "POST" and request.is_ajax():
        ingredient = Ingredient.objects.get(id = form.cleaned_data['id'])
        if ingredient.recipe.id != form.cleaned_data['recipe_id']:
            return _respond('failure')
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return _respond('success')
    else:
        return _respond('failure')

@login_required
def edit_step(request):
    if request.method = "POST" and request.is_ajax():
        step = Step.objects.get(id = form.cleaned_data['id'])
        if step.recipe.id != form.cleaned_data['recipe_id']:
            return _respond('failure')
        form = StepForm(request.POST)
        if form.is_valid():
            form.save()
            return _respond('success')
    else:
        return _respond('failure')

def delete_ingredient(request):
    if request.method = "POST" and request.is_ajax():


def delete_equipment_item(request):
    pass

def delete_step(request):
    pass

def add_recipe_to_docket(request):
    pass

def remove_recipe_from_docket(request):
    pass

