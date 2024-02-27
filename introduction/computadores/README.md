# Computadores

## Problem Statement

Em uma discussão entre amigos, depois de Juquinha afirmar que o fato de um algoritmo ser mal otimizado não importava quando se tinha uma máquina potente e de última geração, Arthur, aluno de algoritmos retrucou seu colega dizendo que até mesmo computadores de última geração poderiam sofrer grandes atrasos caso utilizado um algoritmo péssimo. Para encerrar essa discussão, calcule o tempo de execução dos algoritmos fornecidos no input com uma quantidade N de instruções em um computador que tem uma capacidade X de instruções por segundo.

> **Objetivo**: dizer qual computador vai ser mais rápido dada uma entrada de tamanho N.

> **Complexidades utilizadas**: 2n^2, n.logn, 2^n e n. (Log base 10)

> **Dica**: Utilize o módulo math de Python para ajudá-lo nos cálculos.

obs1: Fórmula pro cálculo da questão → qtd_instruções / instruções por segundo do PC

obs2: considere até 2 casas decimais no cálculo.

## Input

> Cada entrada terá 3 linhas.

> Inicialmente você receberá um valor fixo N que corresponde a quantidade de instruções que serão rodadas.

> Em seguida você receberá o nome de um computador X, uma capacidade Y de instruções por segundo desse computador X e por último o nome do algoritmo e sua complexidade (separados por hífen, como no exemplo a seguir).

> Outra entrada para um segundo computador Z.

**EXEMPLO**:

1000 → (Quantidade de instruções)
Computador X - 10.000 - Algoritmo - n^2
Computador Z - 100.000 - Algoritmo 2 - n^3

## Output

Depois de calculada as velocidades e ver qual é menor, você *imprimirá**:

Velocidade do Computador1: T segundos
Velocidade do Computador2: T segundos
O ComputadorX foi mais rápido!

## Examples

Case: 1
```markdown

Input

1000
ComputadorA - 10000 - Bubble_sort - 2n^2
ComputadorB - 1000 - Mergesort - n.logn

Output

Velocidade do ComputadorA: 200.00 segundos
Velocidade do ComputadorB: 3.00 segundos
O ComputadorB foi mais rápido!
```

Case: 2
```
Input

20
ComputadorC - 10000 - Torre_de_Hanói - 2^n
ComputadorD - 100 - Busca_Linear - n

Output

Velocidade do ComputadorC: 104.86 segundos
Velocidade do ComputadorD: 0.20 segundos
O ComputadorD foi mais rápido!
```