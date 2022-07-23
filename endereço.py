dados = ["nome", "logradouro", "numero", "complemento", "bairro", "cep","cidade", "estado", ]
dados_usuarios ={}

for dado in dados:
    pergunta = "por favor insira seu " + dado +": "
    dados_usuarios[dado] = input(pergunta)





carta = """
{nome}           
{logradouro}, {numero}, {complemento}
{bairro}
{cep} {cidade}, {estado}
"""
print(carta.format(
nome=dados_usuarios["nome"],
logradouro=dados_usuarios["logradouro"],
numero=dados_usuarios["numero"],
complemento=dados_usuarios["complemento"],
bairro=dados_usuarios["bairro"],
cep=dados_usuarios["cep"],
cidade=dados_usuarios["cidade"],
estado=dados_usuarios["estado"],
))


