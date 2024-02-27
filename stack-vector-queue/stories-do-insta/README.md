Stories do Insta

## Problem Statement

Mark Zuckerberg, após sair da aula de algoritmos, foi olhar o instagram e se sentiu incomodado com o fato de que os stories que apareciam no começo da lista eram de perfis com os quais ele não interagia, e os perfis das pessoas mais próximas dele estavam misturadas pelo final da fila. Incomodado, ele buscou alunos da sua turma para arrumarem este problema para ele, pedindo para que o método utilizado para organizar os stories que vão aparecer é de acordo com as ultimas pessoas que ele seguiu e com os perfis com os quais ele interage, sabendo que todos os perfis que ele segue postam stories diariamente e ele usa o instagram no final do dia, após todos já terem postado. Portanto, faça um código que implemente uma lista para organizar os perfis que aparecem, sabendo que quando mark segue um usuário X, X é posto no topo da lista de prioridade, o mesmo acontece quando mark interage com um perfil, comentando ou curtindo o story, e caso ele deixe de seguir o usuário, ele deve sair da lista de stories que aparecem para markinho, o código encerra quando Mark fechar o aplicativo do insta, quando isso acontecer deverá ser impresso a ordem atual da sequência, que aparecerá para ele no dia seguinte.

- ATENÇÃO!!! Responder usando lista duplamente encadeada, também está proibido o uso de bibliotecas
##Input

Mark seguiu Sergio Mark seguiu Kiev Mark seguiu Neymar Mark curtiu o story de Sergio Mark fechou o instagram

##Output
Sergio Neymar Kiev

## Examples
Case: 1
```

Input 
Mark seguiu Neymar
Mark seguiu Grafite
Mark seguiu Messi
Mark seguiu Sergio
Mark curtiu o story de Messi
Mark curtiu o story de Neymar
Mark curtiu o story de Grafite
Mark comentou no story de Messi
Mark seguiu Cr7
Mark fechou o instagram

Output
Cr7
Messi
Grafite
Neymar
Sergio
```

Case: 2
```

Input
Mark seguiu Sergio
Mark seguiu Bruna
Mark seguiu Antonio
Mark seguiu Geydson
Mark seguiu Fred
Mark seguiu Rafael
Mark curtiu o story de Sergio
Mark curtiu o story de Bruna
Mark curtiu o story de Geydson
Mark deixou de seguir Geydson
Mark seguiu Geydson
Mark fechou o instagram

Output
Geydson
Bruna
Sergio
Rafael
Fred
Antonio
```

Case: 3
```

Input 
Mark seguiu Alceu
Mark seguiu Coldplay
Mark seguiu Kanye
Mark seguiu Harry
Mark curtiu o story de Harry
Mark curtiu o story de Alceu
Mark curtiu o story de Coldplay
Mark deixou de seguir Kanye
Mark seguiu Taylor
Mark fechou o instagram

Output
Taylor
Coldplay
Alceu
Harry
```
