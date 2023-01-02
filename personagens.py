from random import randint

class Personagem:
    def __init__(self, vida, mana, valores_dados):
        self.vida = vida
        self.mana = mana
        self.valores_dados = valores_dados

    def dano(self,damage):
        self.vida = self.vida - damage


class Inimigo(Personagem):
    def roletar_dado(self):        
        d = randint(1, 2)
        num = Dado(d, self.valores_dados)
        res = num.rodar()
        print(f'O inimigo escolheu o dado {d} - [{self.valores_dados[d-1]}] e sorteou o número {res}')
        return int(res)



class MyPlayer(Personagem):
    def escolher_dado(self, d):
        self.d = d
        num = Dado(self.d, self.valores_dados)
        res = num.rodar()
        print(f'O dado {self.d} sorteou o número {res}')
        return int(res)
        


class Dado:
    def __init__(self, d, valores):
        self.valores = valores
        self.d = d - 1

    def rodar(self):
        num = randint(0, len(self.valores[self.d])-1)
        print(self.valores[self.d])
        return self.valores[self.d][num]


