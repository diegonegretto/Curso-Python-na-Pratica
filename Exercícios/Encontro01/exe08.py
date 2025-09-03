"""
8. FizzBuzz
Imprima os valores de `1` a `100` usando um laço `for`. Para os números múltiplos de 3,
imprima “Fizz” ao invés do número, para os múltiplos de 5 imprima “Buzz” e para os
múltiplos de 3 e 5, imprima “FizzBuzz”.
Exemplo:
1 2 Fizz 4 Buzz Fizz 7 8 Fizz 10 11 Fizz 13 14 FizzBuzz …
"""

for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz", end=" ")
    elif i%3 == 0:
        print("Fizz", end=" ")
    elif i%5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")


