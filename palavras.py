
lista_letras = []
for i in range(ord("A"), ord("Z") + 1):
    lista_letras.append(chr(i))


def escolhendo_funcao():
    """escolhendo entre criptografar ou descriptografar uma mensagem - não são esperados paremetros"""
    escolha = -1
    while escolha < 0 or escolha > 3:
     escolha = int(input("""\tEscolha um número:
     1 - CRIPTOGRAFAR
     2 - DESCRIPTOGRAFAR\n -> """))
return escolha


escolha = -1
while escolha < 0 or escolha > 3:
    escolha = int(input("""\tEscolha um número:
          1 - CRIPTOGRAFAR
           2 - DESCRIPTOGRAFAR\n -> """))

while True:
    chave = input("insira a chave para ser usada:\n -> ")
if not chave.isdecimal(): continue
if int(chave) > 0:  
 chave = int(chave)
 break


def coletando_chave():
     """não são esperados parametros. Verificando se a chave é um número inteiro valido"""
while True:
     chave = input("insira a chave para ser usada:\n -> ")
     if not chave.isdecimal():  
          continue
     if int(chave) > 0:
     chave = int(chave)
     break
return chave


mensagem = input("escreva uma mensagem para ser codificada\n ->").upper()


def criptografar(lista_letras, chave, mensagem):


def criptografar(lista_letras, chave, mensagem, escolha):
    """São esparados como parametros, uma lista, um número inteiro e uma string.
      Transforma a string em uma nova cadeia de letras. Trocando a letra por uma que 
      esteja no mesmo número de chaves a frente no alfabeto"""
    codificada = ""
    tamanho_letras = len(lista_letras)
    for letra in mensagem:
        posicao = lista_letras.index(letra)
        
        letra_cod = lista_letras[(posicao + chave) % tamanho_letras]
        codificada += letra_cod
        if letra == " ":
            codificada += " "
            continue
        posicao = lista_letras.index(letra)
        if escolha == 1:
            
            letra_cod = lista_letras[(posicao + chave) % tamanho_letras]
            codificada += letra_cod

        elif escolha == 2:
            letra_cod = lista_letras[(posicao - chave) % tamanho_letras]
            codificada += letra_cod
    return codificada


print(mensagem)
print(criptografar(lista_letras, chave, mensagem))
cript = escolhendo_funcao()
key = coletando_chave()
criptografada = criptografar(lista_letras, key, mensagem, cript)

print("\n", criptografada)
try:
pyperclip.copy(criptografada)
print("\nA mensagem foi copiada para a área de transferencia")
except:
 pass
