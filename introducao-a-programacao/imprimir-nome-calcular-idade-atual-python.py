#Desenvolva um programa que recebe do usuário nome completo e ano de
#nascimento que seja entre 1922 e 2023.

#A partir dessas informações, o sistema mostrará o nome do usuário e a idade 
#que completou, ou completará, no ano atual (2023).

#Caso o usuário não digite um número ou apareça um inválido no campo do ano, 
#o sistema informará o erro e continuará perguntando até que um valor correto seja
#preenchido.


while True:
    nome = input("Digite seu Nome: ")
    if all(c.isalpha() or c.isspace() for c in nome):
        break
    else:
        print("Nome inválido! Digite somente Letras e Espaços")
        
while True:
    sobrenome = input("Digite seu Sobrenome: ")
    if all(c.isalpha() or c.isspace() for c in sobrenome):
        break
    else:
        print("Sobrenome inválido! Digite somente Letras e Espaços")

while True:
    try:
        dia_nasc = int(input('Digite o dia de seu Nascimento: '))
        if int(dia_nasc) < 1 or int(dia_nasc) > 31:
            print('Informe um Dia Válido!(entre 1 a 31)')
        else:
         break
    except:
        print('Dia inválido! Digite Somente Números')

while True:
    try:
        mes_nasc = int(input("Digite o Mês de seu Nascimento: "))
        if int(mes_nasc) < 1 or int(mes_nasc) > 12:
            print('Informe um Mês válido!(entre 1 a 12)')
        else:
         break
    except:
        print('Mês Inválido! Digite Somente Números')

while True:
    try:
        ano_nasc = int(input("Digite o Ano de seu Nascimento: "))
        if(ano_nasc) < 1922 or int(ano_nasc) > 2023:
            print('Informe um Ano válido!(entre 1922 a 2023)')
        else:
         break
    except:
        print('Ano Inválido! Digite Somente Números')   

while True:
    try:
        dia_atual = int(input ("Digite o Dia atual: "))
        if int(dia_atual) < 1 or int(dia_atual) > 31:
            print('Informe um Dia Válido!(entre 1 a 31)')
        else:
         break
    except:
        print('Dia inválido! Digite Somente Números')

while True:
    try:
        mes_atual = int(input ("Digite o Mês atual: "))
        if int(mes_atual) < 1 or int(mes_atual) > 12:
            print('Informe um Mês válido!(entre 1 a 12)')
        else:
         break
    except:
        print('Mês Inválido! Digite Somente Números')

while True:
    try:
        ano_atual = int(input ("Digite o Ano atual: "))
        if int(ano_atual) != 2023:
            print('Informe um Ano válido!')
        else:
         break
    except:
        print('Ano Inválido! Digite Somente Números')

nome = nome + " " + sobrenome
idade = ano_atual - ano_nasc

linha = '☲' * 50
titulo = '♦ Dados Do Usuário ♦'

print(linha)
print(titulo.center(50))
print(linha)

print("Nome Completo:",nome)
print("Data Nascimento: " + str(dia_nasc), str(mes_nasc), str(ano_nasc) , sep = "/")
print("Sua Idade é",idade,"Anos!")

if mes_nasc > mes_atual or (mes_nasc == mes_atual and dia_nasc>dia_atual):
        idade=idade-1
        print(nome,"⇢ Você Ainda Não Fez Aniversário esse Ano")

elif dia_nasc == dia_atual and mes_nasc == mes_atual:
        print("Parabéns,",nome,"! Hoje é o Seu Aniversário.")       

else:
    print(nome,"⇢ Você Já Fez Aniversário esse Ano.")

print(linha)
