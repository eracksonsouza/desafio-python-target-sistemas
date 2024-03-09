# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e
# retorne uma mensagem avisando se o número informado pertence ou não a sequência.



# IMPORTANTE:

# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;



n = int(input('Digite um número para verificar se pertence à sequência de Fibonacci: '))
t1 = 0
t2 = 1
encontrado = False

print(f"{t1} ➙ {t2}", end="")
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f" ➙ {t3}", end="")
    if t3 == n:
        encontrado = True
        break
    t1 = t2
    t2 = t3
    cont += 1

print(" ➙ FIM")

if encontrado:
    print(f"O número {n} faz parte da sequência de Fibonacci.")
else:
    print(f"O número {n} não faz parte da sequência de Fibonacci.")

