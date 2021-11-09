from random import shuffle
from typing import List
from datetime import datetime
from hashlib import sha512

class Aposta():
    def __init__(self, numeros:List[int], email:str):
        self.email: str =email
        self.numeros: List[int] =numeros
        self.timestamp: datetime = datetime.now()
    @property
    def hash(self):
        return sha512("".join([self.email,
                               str(self.numeros),
                               str(self.timestamp)]).encode()
                      ).hexdigest()
    def __repr__(self):
        return self.email+', '+str(self.numeros)

numeros = list(range(1,61))
def sorteio(lista:List[int]=numeros,quant:int=6)->List[int]:
    shuffle(lista)
    sorteados = lista[:quant]
    sorteados.sort()
    return sorteados

def ganhadores(sorteado:list, apostas:list, max_divergence:int=2) -> list:
    '''
    Compara as apostas com a sequencia vencedora e retorna listas
    de apostas ganhadoras de acordo com a divergencia maxima de
    numeros definidas.
    
            Parameters:
                    sorteado (list[int]): uma lista de inteiros
                    apostas (list[Aposta]): uma lista de Apostas
                    max_divergence (int): um inteiro
                    
            Returns:
                    winners (list[list[Aposta]]): listas de ganhadores
    '''
    winners = []
    for i in range(max_divergence+1):
        winners.append(list())
        list(map(lambda aposta: winners[i].append(aposta) if
        len(set(aposta.numeros) & set(sorteado))==len(sorteado)-i else
        None,apostas))
    return winners


if __name__=="__main__":
    # apostas aleatorias para teste
    print("Apostando...")

    apostas = list(Aposta(sorteio(),"lucas-"+str(a)) for a in
    range(10_000))

    # Sorteando a combinação vencedora
    print("Gerando combinação vencedora...")
    sorteado = sorteio()
    print("Combinação vencedora: ",sorteado)

    # Adicionando um controle
    #print("Adicionando aposta de controle...")
    apostas.append(Aposta(sorteado,"Controle!"))

    # Verifica se dentro das apostas existe vencedores.
    print("Procurando ganhadores...")
    for a in ganhadores(sorteado,apostas):
        print("Ganhadores:",a)
