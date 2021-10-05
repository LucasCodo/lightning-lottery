from random import choice, shuffle
from random import randint


numeros = list(range(1,61))
def sorteio(lista=numeros,quant=4):
    shuffle(lista)
    sorteados = lista[:quant]
    sorteados.sort()
    return sorteados

def ganhadores(sorteado, apostas):
    """
    Essa função testa se uma aposta é vencedora.
    """
    winner = []
    list(map(lambda aposta: winner.append(aposta) if aposta.numeros == sorteado else None,apostas))
    return winner

class aposta():
    def __init__(self, numeros, email):
        self.email=email
        self.numeros=numeros
        pass
    @property
    def hash(self):
        return ""
    def __repr__(self):
        return self.email+', '+str(self.numeros)
# apostas aleatorias para teste
print("Apostando...")
apostas=list(aposta(sorteio(),"lucas-"+str(a)) for a in range(10000))

# Sorteando a combinação vencedora
print("Gerando combinação vencedora...")
sorteado = sorteio()
print("Combinação vencedora: ",sorteado)

# Adicionando um controle
#print("Adicionando aposta de controle...")
#apostas.append(aposta(sorteado,"Controle!"))

# Verifica se dentro das apostas existe vencedores.
print("Procurando ganhadores...")
for a in ganhadores(sorteado,apostas):
    print("Ganhador:",a)

