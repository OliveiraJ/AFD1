estds = input().split(" ")
simb_alfabeto = input().split(" ")
qtd_transicoes = int(input())

transicoes_afd = {}

for estd in estds:
    transicoes_afd[estd] = {}

for i in range(0,qtd_transicoes):
    inicial, caractere, final = input().split(" ")
    
    if caractere not in transicoes_afd[inicial]:
        transicoes_afd[inicial][caractere] = final
        
estd_inicial = input()
estds_finais = input().split(" ")
delta = input().split(" ")

for palavra in delta:
    estd_atual = estd_inicial
    estd_erro = 0
    
    for letra in palavra:
        try:
            estd_atual = transicoes_afd[estd_atual][letra]
        except KeyError:
            estd_erro = 1
            break
    if(estd_erro == 1 or estd_atual not in estds_finais):
        print('N')
    else:
        print('S')