salariobruto = float(input("\ndigite o seu salario para calculo de imposto de renda R$"))

if  salariobruto <= 1903.98:
        imposto = 0
elif salariobruto >= 1903.99 and salariobruto <= 2826.65:
        imposto = 7.5
elif salariobruto >= 2826.66 and salariobruto <= 3751.05:
        imposto = 15.0
elif salariobruto >= 3751.06 and salariobruto <= 4664.68:
        imposto = 22.5
else:
        imposto = 27.5

salarioliquido = salariobruto - ( salariobruto * ( imposto / 100 ) ) 
print("\nSeu salario de R${} com o imposto descontado fica R${:.2f}".format(salariobruto, salarioliquido))