#USANDO MATCH CASE NA CALCULADORA#

# Recebendo dados do usuário e convertendo para número inteiro (int)
print("Interação com usuário")
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

print (f"\n --- Escolha entre as operações a seguir ---")
print("Digite + soma, - subtração, * multiplicação e / divisao")
operacao = (input("Digite o operador: "))

# Processamento das operações
print("\n--- RESULTADOS DAS OPERAÇÕES ---")
match operacao:
   case "+":
      soma = num1 + num2
      print(f"Soma: {num1} + {num2} = {soma}")
   case "-": 
      subtracao = num1 - num2
      print(f"Subtração: {num1} - {num2} = {subtracao}")
   case "*":
      multiplicacao = num1 * num2
      print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")
   case "/":
      divisao = num1 / num2
      print(f"Divisão Real: {num1} / {num2} = {divisao}")
   case _: 
       print(f"\n -- Alguma informação foi digitada errada")