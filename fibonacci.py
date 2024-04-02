def fibonacci (n):
	tempA = int(0)
	tempB = int(0)

	if n == 0:
		return True

	while True:
		tempA, tempB = tempB, tempA + tempB
		if n == tempA:
			return True
		if n < tempA:
			return False






num=int(input("Por favor insira o numero para o teste: "))
if fibonacci:
	print("seu numero esta na sequencia de fibonacci")
else:
	print("seu numero NAO esta na sequencia de fibonacci")