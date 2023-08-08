import openai
from decouple import config

def chat_gpt():
    api_key = config('OPEN_AI_KEY')
    openai.api_key = api_key
    prompt = "Você agora é um especialista em dar ideias para microsaas inovadores, com mais de 100 saas lançados e baseado nos exemplos que passei, voce vai me entregar um json com as seguintes keys preenchidas com valores no idioma do brasil e as keys são: 'microsaas_name', 'description', 'short_description', 'how_it_works', 'business_model', 'target_audience', 'competitive_edge' e não retorne nada com aspas simples ou duplas ou ```json quero somente o JSON puro aprenda com suas respostas anteriores e traga algo novo e inusitado"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000
    )

    # Recupere a resposta gerada pelo modelo
    answer = response['choices'][0]['text']
    print(answer)
    return answer
