# 2 reais ou presente misterioso?

## Problem Statement

Natal chegando e papai Noel, sabendo que você está aprendendo métodos de ordenação na cadeira de algoritmos, resolveu inovar na maneira de entregar os presentes, na entrega de um presente misterioso, você precisa ordenar a lista com o método específico, após a lista ordenada você receberá uma maravilhosa surpresa! Sabendo o papai Noel da sua generosidade por ter se comportado bastante no ano de 2023, ele pode te sugerir que você duplique o seu presente, pedindo para que você dobre e passe para o próximo, entregando a lista já ordenada e com os valores duplicados para o próximo colega, exalando o espírito natalino.

Atenção:

Os métodos de ordenação que apareceram nos cases são: Insertion Sort, Quick Sort, Merge Sort, Shell Sort e Selection Sort

OBS:

É proibido o uso de bibliotecas, assim como também é proibido utilizar a função sort para ordenar a lista, a ordenação da lista deve ser feita através do método de ordenação especificado no case, também não é permitido que você utilize outro método para ordenar a lista, ex: ordenar com insertion Sort o case de Quick Sort

##Input

Será informado a lista do seu presente misterioso e o método de ordenação especificado, dentre os métodos possíveis. Também pode ser informado se foi ou não dobrado, caso seja, a lista deve ser retornada de maneira ordenada e com os valores duplicados.

Exemplo:

1, 4, 3, 5, 7, 2, 8, 6, 9
Insertion Sort
dobre!

##Output

Será impresso a lista ordenada, dobrada ou não, dependendo do que foi informado.

Exemplo:

[2, 4, 6, 8, 10, 12, 14, 16, 18]

##Examples

Case: 1
```
Input
1, 2, 3, 5, 4
Insertion Sort
não dobre!

Output
[1, 2, 3, 4, 5]
```

Case: 2

```
Input
8, 14, 3, 12, 7, 5, 10, 1, 13, 6, 9, 2, 15, 4, 11
Merge Sort
não dobre!

Output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
```

Case: 3

```
Input
1, 2, 10, 22, 201, 55, 33
Shell Sort
dobre!

Output
[2, 4, 20, 44, 66, 110, 402]
```

Case: 4

```
Input
10, 20, 30, 40, 2, 50
Selection Sort
dobre!

Output
[4, 20, 40, 60, 80, 100]
```

Case: 5

```
Input
23, 12, 123, 15, 22
Quick Sort
dobre!

Output
[24, 30, 44, 46, 246]
```