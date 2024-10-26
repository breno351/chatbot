def saudações(nome):
    import random
    frases = ['bom dia meu nome é' + nome + '.como vai você','olá','oi, tudo bem?']
    print (frases[random.randint(0,2)])
def recebetexto():
    texto = 'cliente: ' + input('cliente: ')
    palavraproibida =['burro','bocó','idiota']
    for p in palavraproibida:
        if p in texto:
            print('boca suja!')
            return recebetexto()
        return texto
def buscaresposta(nome,texto):
    with open('bd.txt' , 'a+') as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != '':
                if texto.replace('cliente ' , ''):
                    print(nome + ':volte sempre')
                return "fim"
            elif viu.strip() == texto.strip():
                proximalinha = conhecimento.readline()
                if "chatbot: " in proximalinha:
                    return proximalinha
                else:
                    print("me desculpa, não sei oque responder!")
                    conhecimento.write("\n" + texto)
                    resposta_user = input("Oque espera de resposta?\n")
                    conhecimento.write('\n' + 'chatbot' + resposta_user)
                    return "Entendi eu aprendi ..."
def exiberesposta(resposta, nome):
    print(resposta.replace("chatbot", nome))
    if resposta == "fim":
        return "fim"
    return "continua"
def exiberesposta_GUI(resposta, nome):
    return resposta.replace("chatbot", nome)
def saudacao_GUI(nome):
    import random
    frases = ['bom dia meu nome é' + nome + '.como vai você','olá','oi, tudo bem?']
    return frases[random.randint(0,2)]
def salva_sugestao(sugestao):
    with open("bd.txt", "a+") as conhecimento:
        conhecimento.wirte("chatbot: "+ sugestao +"\n")
def buscaresposta_GUI(nome,texto):
    with open('bd.txt' , 'a+') as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != '':
              jaccard(texto, viu) >0.3
              proximalinha = conhecimento.readline()
              if "chatbot: " in proximalinha:
                return proximalinha
              else:
                conhecimento.write(texto)
                return("me desculpa, não sei oque responder!")

def jaccard(textousuario, textobase):
    textousuario = limpa_frase(textousuario)
    textobase = limpa_frase(textobase)
    if len(textobase) <1: return 0
    else:
        palavra_em_coumum = 0
        for palavra in textousuario.split():
            if palavra in textobase.split():
                palavra_em_coumum +=1
        return palavra_em_coumum /(len(textobase.split()))
def limpa_frase(frase):
    tirar = ['?', '!', '...', ',', '.', '\n']
    for t in tirar:
        frase = frase.replace(t, " ")
    frase = frase.upper()
    return frase