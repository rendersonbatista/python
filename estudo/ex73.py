numero = (
    "zero", "um", "dois", "três", "quatro", "cinco", 
    "seis", "sete", "oito", "nove", "dez", 
    "onze", "doze", "treze", "quatorze", "quinze", 
    "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)

numerosNormais = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

numUser = int(input(f"Digite um número que estar entre (0) e (20): "))

if numUser == numerosNormais:
    print(f"Você digitou {numero[numUser]}")

while numUser != numerosNormais[0:]:

    numUser = int(input(f"Tente novamente. Digite um número que estar entre (0) e (20): "))

