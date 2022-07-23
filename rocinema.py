

def recebeEntradaInteiro(orientacaoUsuario):
    while True:
        entrada = input(f"{orientacaoUsuario}")
        if (not entrada.isdecimal()):       
            print("Por favor me repasse apenas numeros!")
        else:
            break
    return entrada  
def mostraOcupacaoCinema(vetor):
    print("Ocupacao atual do cinema")
    numero_assento = 1
    for situacao in vetor:
        print(f"Assento {numero_assento}: {situacao} ")
        numero_assento = numero_assento +1

print("\n CINEMA AMOR DE DEUS  \n")

lugares = recebeEntradaInteiro("Digite o numero total de assentos disponiveis: ")
lugares = int(lugares)

vetorLugares = ["-"]*lugares

mostraOcupacaoCinema(vetorLugares)

while True:
    assento = recebeEntradaInteiro("Informe o assento desejado, ou '0' (ZERO) para sair: ")
    if assento == str(0):
        break
    else:
        assento = int(assento)

    if assento > len(vetorLugares): 
        print (f"Assento {assento} inexistente. Escolha outro lugar")  
    elif vetorLugares[assento -1] == "-":    
        vetorLugares[assento -1] = 'Reservado'
        if "-" not in vetorLugares:     
            mostraOcupacaoCinema(vetorLugares)
            print ("Cinema lotado já vai começar o seu filme!")
            break   
    else:   
        print (f"Assento {assento} reservado. ops porfavor esolha assento :")
        continue    

    mostraOcupacaoCinema(vetorLugares)