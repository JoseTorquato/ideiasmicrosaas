from django.urls import path
from ideas.views import generate_idea_view
urlpatterns = [
    path('generate_idea/', generate_idea_view, name='generate_idea'),
]