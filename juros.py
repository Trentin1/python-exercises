# Calcule o juros de um depóisto bancário

principal = float(input("Digite o valor do depósito: R$"))
taxa = 0.01
tempo = float(input("Quantos meses deseja aplicar: "))

juros = principal * taxa * tempo
print(f"Os juros acumulados serão de: R${juros:.2f}")

# Desafio Extra!
# Adapte o programa para que ele também calcule e exiba o valor total acumulado ao final da aplicação.
valor_total = principal + juros
print(f"O valor total ao final da aplicação será de R$ {valor_total:.2f}")
