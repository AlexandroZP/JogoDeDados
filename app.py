import personagens
from cores import c

def resultado(player, inimigo, res_p, res_i):
    if res_p > res_i:
        inimigo.dano(res_p - res_i)
        return 'Você ganhou a rodada'

    elif res_i > res_p:
        player.dano(res_i - res_p)
        return 'Você perdeu a rodada'

    elif res_i == res_p:
        return 'A rodada terminou em  empate'

    else:
        return 'ERRO'


def combate(player, inimigo):

    # Medi o tamanho da vida para definir sua cor
    tvp = ivp = 3
    if 5 < player.vida <= 10:
        tvp = 4
    elif player.vida <= 5:
        tvp = 2

    if 5 < inimigo.vida <= 10:
        ivp = 4
    elif inimigo.vida <= 5:
        ivp = 2

    print(f'Sua vida: {player.vida}', f'{c[tvp]}|{c[0]}' * player.vida, end=' ')
    print(f'    Inimigo: {inimigo.vida}', f'{c[ivp]}|{c[0]}' * inimigo.vida)

    # Checa se o jogador escolheu um valor válido
    while True:
        slct_dado = int(input('Qual dado deseja escolher 1 - [3 & 6] ou 2 - [1 - 6]: '))
        res_p = 0
        if slct_dado == 2 or slct_dado == 1:
            res_p = player.escolher_dado(slct_dado)
            break
    res_i = inimigo.roletar_dado()
    print(res_i, res_p)

    # Verifica quem ganhou a rodada
    return resultado(player, inimigo, res_p, res_i)
        


# Programa principal
pers = personagens.MyPlayer(20, 30, [[3,6],[1,2,3,4,5,6]])
enem = personagens.Inimigo(20, 30, [[3,6],[1,2,3,4,5,6]])

while True:
    res = combate(pers, enem)
    print(res)
    if pers.vida <= 0 or enem.vida <= 0:
        print('O Jogo acabou')
        break