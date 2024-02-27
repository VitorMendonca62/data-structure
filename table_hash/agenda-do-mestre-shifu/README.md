#Agenda do mestre Shifu

##Problem Statement

Shifu, um mestre que cuida do grande palácio de Jade, onde moram os Cinco Furiosos e Po, o Dragão Guerreiro, tem uma lista de discípulos que precisa encaixar em sua agenda para dar aulas de kung fu. Para isso, ele precisaria selecionar seus alunos para certos dias, em grupos ou não. No entanto, ele é um panda vermelho muito atarefado e não tem tempo para isso. Por isso, ele deu essa missão a VOCÊ, jovem mestre de Algoritmos e Estrutura de Dados.


>Na lista de discípulos, cada nome será representado por uma letra:
> >Ex: ‘acabbaa’
> ‘a’ é um nome, ‘c’ é um nome, segundo ‘a’ é outro nome diferente do primeiro 'a' e assim em diante…


> Ao passar suas listas, ele citou algumas regras:
> - O mesmo discípulo não pode ter duas aulas no mesmo dia, esse será o requisito para divisão de grupos; Em um dia pode ter um grupo, trio, dupla ou uma só pessoa, não é definido, desde que não tenha repetição de alunos;
> 
>A divisão de grupos da lista ‘acabbaa’ será:
‘a,c’, ‘a,b’, ‘b,a’, ‘a’


> - Depois de divididos, cada grupo terá seu valor, que corresponderá a soma dos valores ASCII de cada letra;
>
> Ex:
> O grupo ‘a, b’ terá um valor: 97 + 98 = 195

> - Minha agenda sempre terá 10 dias disponíveis, então você terá que se basear nesse número e no valor de cada grupo para encontrar um dia para encaixar um grupo;
>
> Dica: usar mod 10

> - Nos dias que sobrarem, deverá estar escrito ‘vago’;
>
> ['vago', 'vago', 'vago', 'vago', 'vago', ['a', 'b'], ['a', 'c'], ['b', 'a'], ['a'], 'vago']

> - Se o grupo de discípulos cair em uma dia que já está ocupado, você deverá passar esse grupo para um dia depois. Se estiver ocupado até o último dia, você deve recomeçar a lista para procurar um dia vago. Todos os grupos devem ter um dia agendado.
>
> Ex:
>Na lista: ‘a,b’, ‘a,c’, ‘b,a'
>Os dois ‘a,b’ e 'b, a' cairão no mesmo dia, então você deverá passar para o próximo dia vago: [['a', 'b'], ['a', 'c'], ['b', 'a']]

> - Eu o obrigo a usar o conceito de tabela hash para dividir a string dada em grupos e também para encaixar cada um deles em minha agenda.

> - Pode usar lista (Python List)
> - Não pode usar dicionário (Python dict)
> - Atenção com o uso excessivo de trechos com O(nˆ2)
> - Obrigatório usar Tabela Hash

##Input

O input será uma string com várias letras

> hdklqkcssgxlvehva

obs:

a divisão seria: (hdklq),(kcs),(sgxlveh),(va)

## Output

Será a lista dos grupos divididos em seus supostos dias (índices)

>[‘vago’, ['k', 'c', 's'], ['h', 'd', 'k', 'l', 'q'], ‘vago’, ‘vago’, ['v', 'a'], ‘vago’, ‘vago’, ‘vago’, ['s', 'g', 'x', 'l', 'v', 'e', 'h']]

##Examples

Case: 1
```
Input
hdklqkcssgxlvehva

Output
['vago', ['k', 'c', 's'], ['h', 'd', 'k', 'l', 'q'], 'vago', 'vago', ['v', 'a'], 'vago', 'vago', 'vago', ['s', 'g', 'x', 'l', 'v', 'e', 'h']]
```

Case: 2

```
Input
acabbaa

Output

['vago', 'vago', 'vago', 'vago', 'vago', ['a', 'b'], ['a', 'c'], ['b', 'a'], ['a'], 'vago']
```