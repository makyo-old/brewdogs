from brewdogs.glossary.models import *
from brewdogs.glossary.forms import *
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.templates import RequestContext
from django.contrib.auth.decorators import login_required

def list_terms(request):
    pass

def create_term(request):
    pass

def show_term(request, term):
    pass

def edit_term(request, term):
    pass

def delete_term(request, term):
    pass
