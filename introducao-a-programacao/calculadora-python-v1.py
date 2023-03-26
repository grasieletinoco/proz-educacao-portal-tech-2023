#Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a operação a ser executada. Considera a seguinte definição:
#(1 - Soma,  2 - Subtração,  3 - Multiplicação,  4 - Divisão)
#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0

def calculadora(num1, num2, operacao):
    
   if(operacao == 1):
       resultado = num1 + num2
       print("Adição:",num1, "+", num2, "=", resultado)
    
   elif(operacao == 2):
       resultado = num1 - num2
       print("Subtração:",num1, "-", num2, "=", resultado)

   elif(operacao == 3):
       resultado = num1 * num2
       print("Multiplicacão:",num1, "x", num2, "=", resultado)

   elif(operacao == 4):
       resultado = num1 / num2
       print("Divisão:",num1, "/", num2, "=", resultado)

   else: 
       resultado = 0
       print("Operação Inválida = ", resultado)

print("="*30)
calculadora(40, 20, 1)
calculadora(40, 20, 2)
calculadora(40, 20, 3)
calculadora(40, 20, 4)
calculadora(40, 20, 5)
print("="*30)