print("exercicio de fibonacci")
var = int(input("digite a quantidade de numeros  fibonacci  que voçe quer calcular "))

# n + 1 = n + n-1       nota
anterior = 0
proxima = 1
soma = 1

for n  in range (anterior, var ):
    print (anterior)
    soma = proxima + anterior
    anterior = proxima
    proxima = soma