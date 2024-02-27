#Catálogo de livros

##Problem Statement

Os estudantes matriculados na disciplina de Algoritmos e Estruturas de Dados foram convocados pelos gestores da biblioteca para contribuir na construção de um catálogo digital de livros. Para esta tarefa, será empregada uma estrutura de árvore binária. Cada livro será identificado por um número inteiro único, representando sua entrada no catálogo.

A biblioteca fornecerá uma lista de livros, cada um associado a um número inteiro distinto, e sua missão é desenvolver um algoritmo eficiente para inserir esses livros no catálogo. Uma vez que o catálogo esteja completo, solicita-se que apresentem a estrutura da árvore resultante em ordem, proporcionando aos usuários uma visualização organizada e acessível dos livros disponíveis na biblioteca.

##Input

Uma lista de livros representados por números inteiros:

Ex.:
```
     10
    /  \
   5    15
  / \     \
 3   7     20
```
>10 5 3 7 15 20

##Output

Uma lista representando o catálogo pronto organizado ¨em ordem¨.

Ex.:

>3 5 7 10 15 20

##Examples

Case: 1
```
Input
10 5 3 7 15 20

Output
3 5 7 10 15 20
```

Case: 2

```
Input
8 3 1 6 4 10 14

Output
1 3 4 6 8 10 14
```