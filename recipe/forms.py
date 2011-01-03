from brewdogs.recipe.models import *
from django.forms import ModelForm

class CategoryForm(ModelForm):
    class Meta:
        model = Category

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'category', 'batch_size', 'original_gravity', 'target_gravity', 'color', 'notes', 'visible')

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient

class StepForm(ModelForm):
    class Meta:
        model = Step
