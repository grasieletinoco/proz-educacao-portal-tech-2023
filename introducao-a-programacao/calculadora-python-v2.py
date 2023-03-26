#Faça uma função calculadora que os números e as operações serão feitas pelo usuário.
#O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair.
#No início, o programa mostrará a seguinte lista de operações:

#1 - Soma
#2 - Subtração
#3 - Multiplicação
#4 - Divisão
#0 - Sair

#Digite o número para a operação correspondente e caso o usuário introduza qualquer outro,
#o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.
#Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor,
#um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o 
#usuário escolher a opção “Sair”, o sistema irá parar. É necessário que o sistema mostre 
#as opções sempre que finalizar uma operação e mostrar o resultado.

print("Calculadora Python V2\n")
print ("Selecione Qual Das Seguintes Operações Você Quer Executar: ")
print ("1 - Soma")
print ("2 - Subtração")
print ("3 - Multiplicação")
print ("4 - Divisão")
print ("0 - Sair\n")

def calculadora(operacao, num1, num2):
  if (operacao == 1): 
    resultado = (num1 + num2)
  elif (operacao == 2):
    resultado = (num1 - num2)
  elif (operacao == 3):
    resultado = (num1 * num2)
  elif (operacao == 4): 
    resultado = (num1 / num2)
  return resultado

continua = False
while (continua == False):
  try:
    operacao = int(input("Digite O Número Da Operação Desejada: "))

    if (operacao == 0):
      print ('Você Solicitou Sair!')
      continua = True

    elif (operacao != 1) and (operacao != 2) and (operacao != 3) and (operacao != 4):
      print ('Essa Não É Uma Operação Válida!')

    else:  
      num1 = float(input("Digite O Primeiro Número: "))
      num2 = float(input("Digite O Segundo Número: "))

      total = calculadora(operacao, num1, num2)

      if (operacao == 1):
       print('Resultado Da Soma:', num1,"+",num2,"=", total)
       print('\n')

      elif (operacao == 2):
       print('Resultado Da Subtração:', num1,"-",num2,"=", total)
       print('\n')

      elif (operacao == 3):
       print('Resultado Da Multiplicação:', num1,"*",num2,"=", total)
       print('\n')

      else: 
       operacao == 4
       print('Resultado Da Divisão:', num1,"/",num2,"=", total)
       print('\n')

  except:
    print('Você Precisa Digitar Um Número Inteiro')

print ('Fim Da Operação!')