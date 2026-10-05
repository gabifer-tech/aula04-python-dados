#Calculadora com uso de IF
#Autor:
#Data ultima atualização


# Recebendo dados do usuário e convertendo para número inteiro (int)
print("Interação com usuário")
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

print (f"\n --- Escolha entre as operações a seguir ---")
print("Digite + soma, - subtração, * multiplicação e / divisao")
operacao = (input("Digite o operador: "))

# Processamento das operações
print("\n--- RESULTADOS DAS OPERAÇÕES ---")
if operacao == "+":
  soma = num1 + num2
  print(f"Soma: {num1} + {num2} = {soma}")
elif operacao == "-": 
    subtracao = num1 - num2
  print(f"Subtração: {num1} - {num2} = {subtracao}")
elif operacao == "*":
    multiplicacao = num1 * num2
  print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")
elif operacao == "/":
    divisao = num1 / num2
   print(f"Divisão Real: {num1} / {num2} = {divisao}")
else: 
   print(f"\n -- Alguma informação foi digitada errada)



# Exibição formatada dos resultados
print("\n--- RESULTADOS DAS OPERAÇÕES ---")
print(f"Soma: {num1} + {num2} = {soma}")
print(f"Subtração: {num1} - {num2} = {subtracao}")
print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")
print(f"Divisão Real: {num1} / {num2} = {divisao}")
