from brewdogs.recipe.models import *
from brewdogs.recipe.forms import *
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.templates import RequestContext
from django.contrib.auth.decorators import login_required

def list_categories(request):
    """
    List the categories of recipes
    """
    #TODO Paginate
    categories = Category.objects.all()
    return render_to_response("recipe/category/list.html", context_instance = RequestContext(request, {'categories': categories}))

def show_category(request, slug):
    """
    Show detailed information about the category and all associated recipes
    """
    category = get_object_or_404(Category, slug = slug)
    return render_to_response("recipe/category/show.html", context_instance = RequestContext(request, {'category': category}))

@login_required
def edit_category(request, slug):
    """
    Edit the category
    """
    if request.user.has_perm("recipe.can_edit_category"):
        category = get_object_or_404(Category, slug = slug)
        form = CategoryForm(instance = category)
        if request.method == "GET":
            return render_to_response("recipe/category/edit.html", context_instance = RequestContext(request, {'form': form}))
        else:
            form = ArticleForm(request.POST, instance = category)
            if form.is_valid():
                category = form.save()
                request.user.message_set.create('<div class="success">Category saved</div>')
                return redirect(category)
            else:
                return render_to_response("recipe/category/edit.html", context_instance = RequestContext(request, {'form': form}))
    else:
        return render_to_response("errors/403.html", context_instance = RequestContext(request, {}))
                
@login_required
def delete_category(request, slug):
    """
    Delete the category
    """
    if request.user.has_perm("recipe.can_delete_category"):
        category = get_object_or_404(Category, slug = slug)
        category.delete()
        categories = Category.objects.all()
        request.user.message_set.create('<div class="success">Category deleted</div>')
        return render_to_response("recipe/category/list.html", context_instance = RequestContext(request, {'categories': categories}))
    else:
        return render_to_response("errors/403.html", context_instance = RequestContext(request, {}))

@login_required
def create_category(request):
    """
    Create a new category
    """
    if request.user.has_perm("recipe.can_create_category"):
        form = CategoryForm()
        if request.method == "GET":
            return render_to_response("recipe/category/edit.html", context_instance = RequestContext(request, {'form': form}))
        else:
            form = CategoryForm(request.POST)
            if form.is_valid():
                category = form.save()
                return redirect(category)
            else:
                return render_to_response("recipe/category/edit.html", context_instance = RequestContext(request, {'form': form}))
    else:
        return render_to_response("errors/403.html", context_instance = RequestContext(request, {}))

def list_recipes(request):
    """
    List all recipes
    """
    #TODO Paginate
    recipes = Recipe.objects.all()
    return render_to_response("recipe/recipe/list.html", context_instance = RequestContext(request, {'recipes': recipes}))

def show_recipe(request, id):
    """
    Show the recipe
    """
    recipe = get_object_or_404(Recipe, id = id)
    return render_to_response("recipe/recipe/show.html", context_instance = RequestContext(request, {'recipe': recipe}))

@login_required
def edit_recipe(request, id):
    """
    Edit the recipe
    """
    recipe = get_object_or_404(Recipe, id = id)
    if request.user == recipe.owner or request.user.has_perm("recipe.can_edit_recipe"):
        pass
    else:
        return render_to_response("errors/403.html", context_instance = RequestContext(request, {}))

@login_required
def delete_recipe(request, id):
    """
    Delete the recipe
    """
    recipe = get_object_or_404(Recipe, id = id)
    if request.user.has_perm("recipe.can_delete_recipe"):
        recipe.owner.message_set.create('<div class="failure">Your recipe %s has been deleted.  Please contact an administrator if you feel this has been done in error</div>' % recipe.name)
        request.user.message_set.create('<div class="success">You have deleted recipe %s.</div>' % recipe.name)
        recipe.delete()
        return redirect("/recipe/list/")
    else:
        return render_to_response("errors/403.html", context_instance = RequestContext(request, {}))

@login_required
def create_recipe(request):
    """
    Create a recipe
    """
    if request.method == "GET":
        recipe = Recipe(owner = request.user)
        recipe.save()
        form = RecipeForm(instance = recipe)
        return render_to_response("recipe/recipe/edit.html", context_instance = RequestContext(request, {'form': form, 'recipe': recipe}))
    else:
        recipe = Recipe.objects.get(id = request.POST['id'])
        form = RecipeForm(request.POST, instance = recipe)
        if form.is_valid():
            recipe = form.save()
            request.user.message_set.create('<div class="success">Recipe created</div>')
            return redirect(recipe)
        else:
            return render_to_response("recipe/recipe/edit.html", context_instance = RequestContext(request, {'form': form, 'recipe': recipe}))
