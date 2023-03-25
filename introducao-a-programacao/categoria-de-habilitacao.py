#Desenvolva um código que utilize as seguintes características de um veículo:
#- Quantidade de rodas;
#- Peso bruto em quilogramas;
#- Quantidade de pessoas no veículo.

#Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
#A: Veículos com duas ou três rodas;
#B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
#C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
#D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; E: Veículos com quatro rodas ou mais e com mais de 6000 kg.

#RESOLUÇÃO:

quantRodas = int(input("Digite a quantidade de rodas do veículo: "))
peso = int(input("Digite o peso bruto em quilogramas do veículo: "))
quantPessoas = int(input("Digite a quantidade de pessoas que cabem no veículo: "))

if (quantRodas == 2 or quantPessoas == 3):
  print("Categoria de Habilitação do Veículo: A")

elif (quantRodas == 4 and peso <= 3500 and quantPessoas <= 8):
  print("Categoria de Habilitação do Veículo: B")

elif (quantRodas >= 4 and peso >= 3500 and peso <= 6000):
  print("Categoria de Habilitação do Veículo: C")

elif (quantRodas >= 4 and quantPessoas > 8):
  print("Categoria de Habilitação do Veículo: D")

elif (quantRodas >= 4 and peso > 6000):
  print("Categoria de Habilitação do Veículo: E")

else:
  print("Sem Categoria")