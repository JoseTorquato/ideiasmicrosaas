from django.forms import ValidationError
from django.shortcuts import render
from django.contrib import messages

from ideas.models import Ideas, NewsLetter

def home_view(request):
    if request.method == 'POST':
        email = request.POST.get('email-newsletter', '').strip()
        if email:
            try:
                newsletter = NewsLetter(email=email)
                newsletter.full_clean()
                newsletter.save()
                messages.success(request, 'Email cadastrado com sucesso!')
            except ValidationError as e:
                if 'email' in e.message_dict and 'News letter com este Email já existe.' in e.message_dict['email']:
                    messages.error(request, 'Email já está cadastrado na newsletter.')
                else:
                    messages.error(request, 'Email inválido. Por favor, forneça um email válido.')
            except Exception as e:
                messages.error(request, 'Email já cadastrado!')
        else:
            messages.error(request, 'O campo de email não pode estar vazio. Por favor, forneça um email válido.')

    data = Ideas.objects.all().order_by('-created_at').values('microsaas_name', 'description', 'short_description', 'how_it_works', 'business_model', 'target_audience', 'competitive_edge')
    return render(request, 'index.html', context={ "ideas": data }) 

def blog_view(request):
    return render(request, 'pages/mixed/blog/details_five_ideas.html') 

def sitemap_view(request):
    return render(request, 'sitemap.xml') 