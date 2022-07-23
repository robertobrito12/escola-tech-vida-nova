
def mostra_pista(pinos):
    for elemento in pinos:  
        print(elemento, end=' ')
    print()

    



pista = [ 
'I', ' ', 'I', '\n',' ', 'I', ' '
]
posicao_dos_pinos = {
'1': 5,
'2': 0,
'3': 2,
}
mostra_pista(pista)




jogada = ['3']

for pino in jogada:
    posicao = posicao_dos_pinos[pino]
    pista[posicao] =  ' '

mostra_pista(pista)