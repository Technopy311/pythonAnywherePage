from django.urls import path
from .views import index, photography, about_me, career, projects

urlpatterns = [
    path('', index, name="index"),
    path('photography/', photography, name="photography"),
    path('about/', about_me, name="about"),
    path('career/', career, name="career"),
    path('projects/', projects, name="projects")
]