from django.shortcuts import render
from ideas.models import Ideas
import json

from ideas.openai import chat_gpt
from ideas.views import save_idea

def home_view(request):
    data = Ideas.objects.all().values('microsaas_name', 'description', 'short_description', 'how_it_works', 'business_model', 'target_audience', 'competitive_edge')
    return render(request, 'index.html', context={ "ideas": data }) 