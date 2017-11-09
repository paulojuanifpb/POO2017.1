def menu():
  print("MENU")
  print("1- ADIÇÃO")
  print("2- SUBTRAÇÃO")
  print("3- MULTIPLICAÇÃO")
  print("4- DIVISÃO")
  print("5- POTENCIAÇÃO")
  print("6- RADICIAÇÃO")
  print("7- SAIR")

def adicao():
   x = int(input('Digite um valor:\n'))
   y = int(input('Digite outro valor:\n'))
   resultado = x+y
   print("RESULTADO: ",resultado)
   
def subtracao():
   x = int(input('Digite um valor:\n'))
   y = int(input('Digite outro valor:\n'))
   resultado = x-y
   print("RESULTADO: ",resultado)

def multiplicacao():
   x = int(input('Digite um valor:\n'))
   y = int(input('Digite outro valor:\n'))
   resultado = x*y
   print("RESULTADO: ",resultado)

def divisao():
   x = int(input('Digite um valor:\n'))
   y = int(input('Digite outro valor:\n'))
   resultado = x/y
   print("RESULTADO: ",resultado)

def potencia():
  x = int(input('Digite um valor para a base:\n'))
  y = int(input('Digite um valor para o expoente:\n'))
  resultado = (x**y)
  print("RESULTADO: ",resultado)
  
def raiz():
   x = int(input('Digite um valor:\n'))
   resultado = x**(1/2)
   print("RESULTADO: ",resultado)
   
   
   
   
   
menu()
continuar = 1
while (continuar == 1):
  op = int(input('Escolha uma das opções:\n'))
  if (op == 1):
    adicao()
  elif (op == 2):
    subtracao()
  elif (op == 3):
    multiplicacao()
  elif (op == 4):
    divisao()
  elif (op == 5):
    potencia()
  elif (op == 6):
    raiz()
  elif (op == 7):
    continuar = 0
   
