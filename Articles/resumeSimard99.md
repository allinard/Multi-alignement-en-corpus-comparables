# Résumé de l'article : Text-Translation Alignment: Three Languages Are Better Than Two
---------

### En quelques mots : 
Cet article répond à la problématique suivante : "Comment une méthode d'alignement bilingue pour la traduction de texte  peut être adaptée pour gérer plus de deux versions d'un texte ?". L'idée est que chaque version additionnelle d'un texte (une langue supplémentaire) apporte de l'information supplémentaire, et que du coup, plus on a de versions d'un texte mieux c'est. Il s'agit de **corpus parallèles**


## Alignement trilingue et méthode générale pour l'alignement de plusieurs versions d'un texte 

Ce qui est considéré ici est l'alignement phrastique pour plusieurs raisons (les concepts présentés dans l'article peuvent néanmoins être appliqués à d'autres niveau de résolution) :

* très utile dans le cadre de beaucoup d'applications (lexicographie bilingue, traduction automatique)
* largement étudié, d'où le fait qu'un certain consensus existe sur comment le problème doit être abordé

En ce qui concerne l'état de l'art, la plupart des algorithmes d'alignement existants (en 1999) peuvent être étendus à N langues.

Une idée pour aligner 3 textes serait, étant donné 3 textes A, B et C, déterminer quelles paires (AB, AC ou BC) est la plus similaire. On aligne la paire la plus semblable, puis ensuite l'autre par rapport à cet alignement. Le problème est donc le suivant :

* Comment mesurer la similarité entre deux versions différentes d'un texte ?
* Qu'est-ce qu'aligner un texte avec un alignement ?

Ce qui est proposé pour mesurer la paire la plus similaire est de calculer le score d'alignement final (un dérivé de la distance d'édition entre 2 chaînes - Gale & Church 91 - disant que deux phrases sont alignables en corpus parallèles si elles ont grosso modo la même longueur), puis d'aligner le texte restant avec la paire déjà alignée, en considérant que l'alignement de la première paire est une séquence d'éléments. Pour cela on calcule la similarité commune des éléments (combinaison linéaire des comparaisons par paire). 


## Expérimentations

Deux expérimentations :

* L'approche décrite ci-dessus
* Une autre, combinant l'alignement basé sur la longueur des phrases et la ressemblance graphèmique (cognats)

Corpus : The Gospel According to John en anglais français et espagnol


