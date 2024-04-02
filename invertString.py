def invert(s):
	string_invertida = ""

	for c in s:
		string_invertida = c + string_invertida

	return string_invertida

s_original = str(input("Por favor insira a string a ser invertida: "))
print(invert(s_original))