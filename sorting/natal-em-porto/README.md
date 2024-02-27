# Natal em porto

##Problem Statement

Havia uma ONG encantadora chamada "CINatal" que tinha um projeto especial para o Natal. Decidiram levar alegria às crianças de Porto de Galinhas, uma bela cidade no litoral nordeste de Pernambuco. A equipe da ONG preparou presentes maravilhosos para distribuir nas praças da cidade.

Ao chegarem a Porto de Galinhas, ficaram encantados com a beleza das praças, cada uma delas única e especial. As praças, no entanto, tinham uma peculiaridade interessante: eram numeradas para indicar sua ordem. As praças são chamadas de Praça 1, Praça 2, Praça 3, e assim por diante.

Enquanto a equipe da ONG CINatal distribuía os presentes nas praças de Porto de Galinhas, souberam que uma emissora de televisão local estava planejando transmitir um especial de Natal, destacando essas ações solidárias. O programa incluiria uma seção especial sobre as doações da ONG, mostrando as praças numeradas e as crianças recebendo os presentes.

Para garantir uma transmissão fluida e impactante, a emissora solicitou à ONG que ordenasse os seus registros de doação, ordenando tanto as praças numericamente quanto uma lista organizada com os nomes das crianças beneficiadas em cada praça. Dessa forma, a audiência poderia acompanhar a distribuição dos presentes de forma mais compreensível e emocionante, destacando o esforço da ONG e a alegria das crianças.

Então, você, aluno da disciplina de Algoritmos, ajudará a ONG a organizar os seus registros de doação criando um algoritmo de ordenação BubbleSort para organizar.

OBS: É obrigatório usar o algoritmo BubbleSort tanto para organizar a ordem das praças quanto para organizar o nome das crianças.

##Input

Você receberá inicialmente um valor indicando a quantidade de praças em que a ONG distribuiu presentes. Em seguida, receberá os nomes das praças seguido das crianças que receberam presentes nela.

##Output

Você deverá printar as praças em ordem numérica crescente e os nomes das crianças em ordem alfabética.

##Examples

Case: 1
```
Input
4
Praça 2: Marcos Ana Lucas
Praça 1: Heitor João Sofia
Praça 3: Maria Jorge Ana
Praça 4: Pedro Clara Gabriel Isabela

Output
Praça 1: Heitor João Sofia
Praça 2: Ana Lucas Marcos
Praça 3: Ana Jorge Maria
Praça 4: Clara Gabriel Isabela Pedro
```

Case: 2
```
Input
8
Praça 2: Lucas Julia Felipe
Praça 5: Isabella Gabriel Manuela
Praça 1: Matheus Ana Gustavo
Praça 6: Rafaela João Mariana
Praça 3: Laura Daniel Sophia
Praça 7: Pedro Carolina Bruno
Praça 4: Maria Thiago Beatriz
Praça 8: Victor Amanda Henrique Larissa

Output
Praça 1: Ana Gustavo Matheus
Praça 2: Felipe Julia Lucas
Praça 3: Daniel Laura Sophia
Praça 4: Beatriz Maria Thiago
Praça 5: Gabriel Isabella Manuela
Praça 6: João Mariana Rafaela
Praça 7: Bruno Carolina Pedro
Praça 8: Amanda Henrique Larissa Victor
```