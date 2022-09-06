### Fase 1
#Risolvi il seguente problema con uno script nel linguaggio di programmazione che preferisci.
#
#```
#I primi dodici numeri della sequenza di Fibonacci sono:
#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
#
#Il 12° numero è il primo della sequenza a essere di 3 cifre.
#Quale è il primo numero della sequenza ad avere 1000 cifre?
#```

import math

index = 0
counter = 2

digits = pow(10, 999)

fibonacciNumber = [1,0,1]

while (fibonacciNumber[index] <= digits) :
    index = (index + 1) % 3
    counter = counter + 1
    fibonacciNumber[index] = fibonacciNumber[(index + 1) % 3] + fibonacciNumber[(index + 2) % 3]

print(counter)