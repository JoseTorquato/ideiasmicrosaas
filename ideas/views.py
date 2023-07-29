from django.shortcuts import redirect
from django.contrib import messages
from ideas.models import Ideas
from ideas.openai import chat_gpt
import json 
def save_idea(data):
    idea = Ideas(
        microsaas_name = data["microsaas_name"],
        description = data["description"],
        short_description = data["short_description"],
        how_it_works = data["how_it_works"],
        business_model = data["business_model"],
        target_audience = data["target_audience"],
        competitive_edge = data["competitive_edge"]
    )
    idea.save()

def generate_idea_view(request):
    ideia_generate = chat_gpt()  
    try:
        save_idea(json.loads(ideia_generate))
        messages.success(request, 'A nova ideia foi gerada com sucesso!')
    except Exception as e:
        print(e)
        messages.error(request, 'Ocorreu um problema ao gerar a nova ideia!')
    return redirect('admin:ideas_ideas_changelist') 