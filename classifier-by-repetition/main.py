from collections import defaultdict

def process_text(text: str):
    return text.lower().split()

def generate_terms(texts: dict):
    terms = defaultdict()

    for entity in texts:
        terms[entity] = defaultdict(int)
        for text in texts[entity]:
            words = process_text(text)
            for word in words:
                terms[entity][word] += 1    
    return terms

def predict_entity(words: list, terms: dict):
    for entity in terms:
        sum_quantity = sum(terms[entity].values())
        total = sum(terms[entity][word] for word in words)

        probability = total / sum_quantity
        print(f"\n{entity}: {probability}")

texts = {
    "anuncios": [
        "Tudo pronto para declarar seu Imposto de Renda!",
        "Clique pra desbloquear +15% OFF",
        "Ninja indica Ofertas INSANAS pra você",
        "Equipe-se pra amassar na #GamePlay",
        "Tech Hub tá #ON com até 65% OFF",
        "Seleção de produtos com boas avaliações",
        "Para combinar com seu pedido",
        "Pra encher Descontos em Periféricos",
        "Plantão de CUPONS Os melhores preços",
        "Conecte-se às melhores ofertas",
        "Hora de Atualizar sua Coleção!",
        "Aproveite nossos Descontos Exclusivos!",
        "Novidades Chegaram: Não Fique de Fora!",
        "Desconto Especial para Clientes VIP!",
        "Descubra Ofertas Incríveis: Acesse Agora!",
        "Renove Seu Guarda-Roupa com Descontos!",
        "Não Deixe Escapar: Ofertas Imperdíveis!",
        "Economize em Todos os Produtos: Confira!",
        "Promoção Relâmpago: Corra e Aproveite!",
        "Estoque Limitado: Garanta Já o Seu!",
    ],
    "social": [
        "Eu gostaria de me conectar",
        "enviou uma mensagem para você",
        "compartilhou uma",
        "Você teve visualizações do perfil",
        "Você tem mensagem nova",
        "marcou seu comentário como",
        "pessoas notaram seu perfil",
        "Compartilhado por seus amigos",
        "Sua postagem está viralizando!",
        "Amigos querem se conectar com você",
        "Fotos marcadas com você",
        "Você foi mencionado em um post",
        "Recebeu novas solicitações de amizade",
        "Novo seguidor: Seja bem-vindo!",
        "Seu vídeo está ganhando destaque",
        "Atualização de status de amigos",
        "Seu perfil está sendo reconhecido!",
        "Postagens recomendadas para você",
        "Notícias importantes da sua rede",
        "Momentos populares entre amigos",
    ]
}


terms = generate_terms(texts)

input_text = "Desconto Exclusivo Economize Agora em Toda a Coleção!"
print("Entrada:", input_text)

words = process_text(input_text)
predict_entity(words, terms)