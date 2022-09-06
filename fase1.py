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

digits = 999

goldenRatio = 1.6180

print(round(((digits * math.log(10)) + (math.log(5)/2))/(math.log(goldenRatio))))