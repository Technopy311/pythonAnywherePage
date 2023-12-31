from django.shortcuts import render
from .models import Photo, Project

def index(request):

    latest_photos = Photo.objects.all()[:5]
    latest_projects  = Project.objects.all()[:5]

    context = {
        "latest_photos": None,
        "latest_projects": None
    }

    if latest_photos.count() > 0:
        context["latest_photos"] = latest_photos

    elif latest_projects.count() > 0:
        context["latest_projects"] = latest_projects


    return render(request, 'core/index.html', context=context)


def photography(request):
    return render(request, 'core/photos.html')


def career(request):
    return render(request, 'core/career.html')


def projects(request):
    return render(request, 'core/projects.html')


def about_me(request):
    return render(request, 'core/about.html')