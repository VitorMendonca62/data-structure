#Fuja do Grinch!

##Problem Statement

Natal está chegando e o maior inimigo do papai Noel, o Grinch, veio para aterrorizar os habitantes de Quemlândia, uma cidade pacífica onde nenhum cidadão possui a mesma idade que qualquer outro, todos tem idades diferentes. Para realizar seus planos maquiavélicos, ele organizou os cidadãos de uma maneira curiosa, a ordem dos documentos dos cidadãos que ele roubou está toda embaralhada, portanto, ele organiza com um heapSort de máximo para conseguir assaltar primeiro o mais velho dos cidadãos e logo após roubar os presentes da pessoa do primeiro documento que ele leu.

No entanto, o papai Noel soube dessa sua nova estratégia e convocou você, aluno de algoritmos do cin, para alertar os cidadãos que estão sob a ameaça de Grinch!

ATENÇÂO: É obrigatório o uso de heapsort de máx, assim como também é proibido o uso de bibliotecas que façam a ordenação bem como é proibido o uso da função max.

##Input

Será disponibilizado uma sequência de números, a qual irá formar a primeira árvore.

EX:

10 20 5 6 23 11 14 3 9

##Output

Será informado um texto dizendo o primeiro alvo de Grinch e o segundo.

Atenção, Grinch está indo atrás do cidadão de 23 anos, e logo após isso ele vai atrás do cidadão de 10 anos.

OBS: Grinch sempre vai partir do novo index 0 da nova lista, listaOrdenada[0], até o index 0 da lista pré ordenada, listaInicial[0]

##Examples

Case: 1
```
Input
10 20 5 6 23 11 14 3 9

Output
Atenção, Grinch está indo atrás do cidadão de 23 anos, e logo após isso ele vai atrás do cidadão de 10 anos.
```

Case: 2
```
Input
55 13 59 10 70

Output
Atenção, Grinch está indo atrás do cidadão de 70 anos, e logo após isso ele vai atrás do cidadão de 55 anos.
```

Case: 3
```
Input
70 34 21 17 56 9 62 2

Output
Atenção, Grinch está indo atrás do cidadão de 70 anos, e logo após isso ele vai atrás do cidadão de 70 anos.
```