# a = float(input('Digite um numero: '))
# b = float(input('Digite um numero: '))

# if a > b:
#     print('primeiro numero é maior que o segundo')
# elif a == b:
#     print('Os numeros são iguais')
# else:
#     print('O segundo numero é maior que o primeiro')

# a = float(input('Digite um numero: '))
# operador = input('Digite o operador: ')
# b = float(input('Digite um numero: '))


# if operador == '+':
#     print(a + b)
# elif operador == '-':
#     print(a - b)
# elif operador == '*':
#     print(a*b)
# elif operador == '/':
#     print(a/b)
# else:
#     print("Operador não existe")

# nota = float(input('Digite a nota do aluno: '))

# if nota >= 7:
#     print('Aprovado')
# elif nota >= 5 or nota < 7:
#     print ('Recuperação')
# else:
#     print('Reprovado')

# lista = [100,500,1800,800,2000,2500]


# meta = 1000
# bonus = 0.1
# for venda in lista:
#     if venda >=1000:
#         valorb = venda * bonus
#         print(valorb)
#     else:
#         print('Não tem bonus')

# numero = int(input("Digite um numero: "))
# soma = 0
# for i in range(1, numero + 1):
#     soma += i
# print(soma)

# numero = 7

# for i in range(10 + 1):
#     resultado = numero * i
#     print(f'{numero} x {i} = {resultado}')

# numero = int(input("Digite um numero: "))

# for i in range(10 + 1):
#     resultado = numero * i
#     print(numero , "x", i , "=" , resultado)

# for i in range(10):
#     print(i)
lista = []
for i in range(5):
    nome = input("Digite um nome: ")
    lista.append(nome)
    print(f'O nome digitado é {nome}')


print(lista)
print(lista[0])