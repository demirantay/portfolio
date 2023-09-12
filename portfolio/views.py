# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.contrib.auth.models import User

# My Module Imports
from .models import Project


def index(request):
    """this is the landing page of the main site
    """
    
    try:
        projects = Project.objects.all().order_by("-id")
    except ObjectDoesNotExist:
        projects = None

    data = {
        "projects": projects,
    }

    return render(request, "home.html", data)
