"""
Código feito para responder a questão 2) do teste gupy da Target

ALISON COSTA 
"""

def fibonacci (n):
	tempA = int(0)
	tempB = int(1)

	if n == 0:
		return True

	else:
		while True:
			tempA, tempB = tempB, tempA + tempB
			if n == tempA:
				return True
			if n < tempA:
				return False


num=int(input("Por favor insira o numero para o teste: "))
if fibonacci(num):
	print("seu numero ESTA na sequencia de fibonacci")
else:
	print("seu numero NAO esta na sequencia de fibonacci")