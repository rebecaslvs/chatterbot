from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONFIGURACOES_CONVERSAS = [
   r"C:\Users\rebec\OneDrive\Área de Trabalho\chatterbot\conversas\saudacoes.json",
    r"C:\Users\rebec\OneDrive\Área de Trabalho\chatterbot\conversas\informacoes_basicas.json"
]

def iniciar():
    global robo
    global treinador

    robo = ChatBot("Sofia")
    treinador = ListTrainer(robo)

def carregar_conversas():
    conversas = []

    for arquivo_configuracao in CONFIGURACOES_CONVERSAS:
        with open(arquivo_configuracao, "r") as arquivo:
            conversas_configuradas = json.load(arquivo)
            conversas.extend(conversas_configuradas["conversas"])
            
            arquivo.close()
    return conversas

def treinar_robo(conversas):
    global treinador

    for conversa in conversas:
        for mensagens_resposta in conversa["mensagem"]:
            mensagem = mensagens_resposta
            resposta = conversa["resposta"]

            treinador.train([mensagem])
            treinador.train([resposta])

if __name__ == "__main__":
    iniciar()

    conversas = carregar_conversas()
    if  conversas:
        treinar_robo(conversas)