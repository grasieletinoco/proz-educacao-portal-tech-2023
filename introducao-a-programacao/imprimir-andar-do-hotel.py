#Escrever um código que imprima um número para cada andar de um hotel de 20 andares, exceto o número 13. Como desafio, imprima eles em ordem decrescente

i = 21

while i > 1:
    i -= 1
    
    if i == 13:
        continue

    print (i," Andar",sep = "º")
print("FIM")

print("\n")



for i in range (20, 0, -1):

	if (i ==13):
		continue
	print (i," Andar",sep = "º")
print("FIM")
