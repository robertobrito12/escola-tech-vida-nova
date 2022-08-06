cpf_original = '145.382.206-20' 

cpf_sem_validacao = 14538220


cpf_copia = cpf_sem_validacao
print("Documento sem verificaçao ', cpf_sem _validaçao")

total = 0
for peso in range(2, 11):
    digito = cpf_sem_validacao % 10
    cpf_copia = cpf_copia // 10
    resultado = digito * peso
    total = total + resultado
    total_mod11 =  total % 11
    digito_var1 = 11- total_mod11

print(total)