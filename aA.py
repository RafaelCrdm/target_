# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
#seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência 
#ou pode ser previamente definida no código;

def string_with_a(string: str) -> list:
	return string.count('a'), string.count('A')

x = string_with_a("banAna mAdurA")
print(f'minusculo: {x[0]}\nmaiusculo: {x[1]}')