from chatterbot import ChatBot
import json
from chatterbot.trainers import ListTrainer

with open('treinamento.json', mode='r', encoding='utf-8') as arquivoTreinamento:
    treinamento = json.load(arquivoTreinamento)

lista_treinamento = treinamento["conversas"]
robo = ChatBot("Sofia")
treinador = ListTrainer(robo)

def treinar_robo():
    lista_completa = []
    for conversa in lista_treinamento:
        for mensagem in conversa["mensagem"]:
            lista_completa.append(mensagem)
            lista_completa.append(conversa["resposta"])
    treinador.train(lista_completa)
    return lista_completa

def input_usuario(dialogo):
    if dialogo: return dialogo
    else: 
        try:
            dialogo = input("Digite a sua pergunta ou digite 'sair' para encerrar o programa: ")
            return dialogo
        except(KeyboardInterrupt, EOFError, SystemExit):
            print("Se tiver qualquer dúvida sobre o renascimento, estou à disposição. Até mais!")
            return False

def iniciar_sofia():
    print("Olá, eu sou a Sofia, sua assistente virtual.")

    while True:
        melhor_confianca = 0.7
        confianca = 0
        dialogo = input_usuario()
        
        if dialogo == False:
            break
        
        if dialogo.lower() == "sair":
            print("Se tiver qualquer dúvida sobre o renascimento, estou à disposição. Até mais!")
            break

        resposta = robo.get_response(dialogo)
        confianca = resposta.confidence
            
        if confianca > melhor_confianca:
            print(f"Confiança: {confianca * 100}%")
            print(resposta)
        else:
            print("Não entendi o que você quis dizer. Poderia reformular a sua pergunta?: ")

if __name__ == "__main__":
    treinar_robo()
    iniciar_sofia()