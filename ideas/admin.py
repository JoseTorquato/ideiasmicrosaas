from django.contrib import admin
from ideas.models import Ideas
from ideas.openai import chat_gpt
from ideas.views import save_idea


class IdeasAdmin(admin.ModelAdmin):
    list_display = ('microsaas_name', 'description', 'created_at', 'updated_at')
    actions = ['generate_new_idea']
    
    def generate_new_idea(self, request, queryset):
        self.message_user(request, "Nova ideia gerada com sucesso.")

admin.site.register(Ideas, IdeasAdmin)
