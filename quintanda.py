precos = {
'Carambola': 7,
'Melancia' : 20,
'Jabuticaba': 1
}

mensagem_pergunta_fruta = """
temos as seguintes frutas:
Melancia
Jabuticaba
Carambola
qual delas vocé gostaria ?
"""
fruta = input(mensagem_pergunta_fruta)
precos_frutas = precos[fruta]
print('o preço unitário dessa fruta é {}'.format(precos_frutas))
quantidade = int(input('quantas unidades voçé gostaria ?\n'))
quantidade_int = int(quantidade)

total = quantidade_int * precos_frutas
print('o total deu {} reais'.format(total))