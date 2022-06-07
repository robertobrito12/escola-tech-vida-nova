


var = int(input("digite a quantidade de numeros de fibonacci que voçe quer calcular "))
anterior = 0
proxima = 1

while proxima < var:
    print(anterior)
    proxima = proxima + anterior
    anterior = proxima - anterior
    if(anterior == 0):
        proxima = anterior + 1
    # enquanto nao chegar na 