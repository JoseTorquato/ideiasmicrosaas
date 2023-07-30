import openai

def chat_gpt():
    # Defina sua chave de API
    api_key = "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"

    # Configure o cliente com sua chave de API
    openai.api_key = api_key

    # Texto de entrada para o GPT-3.5
    prompt = "Você agora é um especialista em dar ideias para microsaas inovadores, com mais de 100 saas lançados e baseado nos exemplos que passei, voce vai me entregar um json com as seguintes keys preenchidas com valores no idioma do brasil e as keys são: 'microsaas_name', 'description', 'short_description', 'how_it_works', 'business_model', 'target_audience', 'competitive_edge' e não retorne nada com aspas simples ou duplas ou ```json quero somente o JSON puro aprenda com suas respostas anteriores e traga algo novo e inusitado"
#     prompt = """
#         Você agora é um especialista em dar ideias para microsaas inovadores, com mais de 100 saas lançados, voce vai me entregar um json com as seguintes keys preenchidas com valores no idioma do brasil e as keys são: 'microsaas_name', 'description', 'short_description', 'how_it_works', 'business_model', 'target_audience', 'competitive_edge'.
#         Aqui estão algumas ideias para você treinar: 
#         . Gerador de descrição de produto com tecnologia de IA
# Programas de IA como ChatGPT e Notion são muito bons para gerar texto para projetos. Seria relativamente fácil criar um aplicativo que usasse o ChatGPT para reescrever descrições de produtos com o toque de um botão.

# Embora essa ideia básica já exista, você poderia dar um passo adiante e criar uma ferramenta de SEO que analisasse automaticamente as palavras-chave que você deveria usar e as incluísse na descrição do produto. Isso seria especialmente útil para lojas de dropshipping que trabalham com muitos produtos de terceiros e desejam uma solução rápida que não exija muito esforço.

# 2. Apps on top-of-a-platform-like-crisp
# Algumas plataformas podem não ter recursos avançados devido à sua posição no mercado.

# De fato, alguns recursos estão mais relacionados a clientes de médio porte ou corporativos. Portanto, essas plataformas têm como alvo as pequenas e médias empresas. É por isso que não é uma prioridade máxima, pois exige muito trabalho profundo.

# Os criadores de micro-saas podem aproveitar essa estratégia para criar um aplicativo sobre uma plataforma em que os usuários já passam muito tempo.

# Aqui estão 5 recursos que você poderia criar como um micro-saas sobre o Crisp marketplace:

# Plugin de SLA que ajuda as empresas a priorizar as conversas. Esse plug-in ajuda a manter-se entre os acordos de nível de serviço que a empresa assinou com seus clientes.
# Plug-in do Google Analytics que ajuda a rastrear automaticamente o impacto de um bate-papo ao vivo na taxa de conversão.
# Plug-in de conversação do Shopify para WhatsApp. Esse recurso é uma grande melhoria em termos de experiência do cliente, pois os comerciantes on-line poderão enviar mensagens automatizadas do WhatsApp para seus clientes em qualquer etapa do ciclo de vida do cliente (pense no status do pedido aqui, por exemplo).
# Plugin de formulário de contato avançado para oferecer um formulário de contato avançado e personalizável a ser incorporado em todo o site
# 3. Aplicativo de gerenciamento de fluxo de trabalho para Slack
# Muitas equipes são totalmente remotas no momento, e muitas delas usam plataformas como Slack e Microsoft Teams para comunicação. Essas ferramentas têm mercados repletos de aplicativos criados sobre a plataforma, o que permite muitos recursos e funcionalidades adicionais.

# Você poderia criar um aplicativo que usasse IA para ajudar as empresas a gerenciar e interagir com suas equipes remotas. Essa ideia é um pouco vaga por natureza porque você precisa validar quais problemas essas empresas estão enfrentando, mas definitivamente há muito potencial no mercado do Slack.

# 4. Uma extensão do Chrome para quem procura emprego
# Você já se candidatou a um emprego on-line e, depois de terminar de carregar seu currículo, ele pediu que você preenchesse toda a sua experiência profissional, um parágrafo de cada vez? No entanto, esses problemas são perfeitos para serem resolvidos por empreendedores. Você pode criar uma extensão do Chrome que use IA para analisar os dados na tela e inserir suas informações automaticamente. Você também pode criar um recurso para sugerir respostas às perguntas que estão sendo feitas aos candidatos ou gerar/melhorar cartas de apresentação.

# Com todas as demissões no início de 2023, pode ser o momento perfeito para lançar essa ideia.

# 5. Aplicativo de envolvimento do funcionário usando arte com IA
# Caso você não tenha percebido, houve uma grande tendência na geração de arte com IA no início deste ano. Bastava fazer o upload de 15 a 25 fotos suas para que a IA pudesse pegar seu rosto e suas características e transformá-lo em todos os tipos de arte. Programas como o Dall-E e o Stable Diffusion podem transformá-lo em um caubói, um astronauta ou o que você quiser.

# Há uma oportunidade de usar esse conceito para criar um aplicativo de engajamento de funcionários em uma plataforma como o Slack. Quando um funcionário atinge suas métricas, o aplicativo pode gerar automaticamente uma imagem visualmente bem-sucedida dele.

# Por exemplo, Dave atingiu sua meta de vendas para o mês, então o aplicativo gerou uma imagem de Dave como um cowboy, já que ele é a arma mais rápida do Oeste. Sarah atingiu uma pontuação de 95% de satisfação do cliente em julho, então o aplicativo gerou uma imagem dela segurando um troféu em uma plataforma nas Olimpíadas.

# Essa é uma ideia divertida que com certeza envolveria os funcionários, especialmente se você pudesse configurá-la para ser muito engraçada ou aleatória.

# Essas ideias de micro saas podem servir como um trampolim para você pensar em suas próprias soluções exclusivas. 
#     """    
   
    # Faz a solicitação para o GPT-3.5
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000
    )

    # Recupere a resposta gerada pelo modelo
    answer = response['choices'][0]['text']
    print(answer)
    return answer
