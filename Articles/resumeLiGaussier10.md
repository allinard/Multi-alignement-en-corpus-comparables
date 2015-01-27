# Résumé de l'article : Improving Corpus Comparability for Bilingual Lexicon Extraction from Comparable Corpora
---------

### En quelques mots : 
Le but des travaux ici est d'améliorer la qualité des corpus comparables utilisé pour la tâche d'extraction de lexiques bilingues en définissant une mesure de comparabilité et une stratégie d'amélioration de la qualité d'un corpus donné. 


## Etat de l'art
Ce qui existe :
* extraction de lexiques bilingues à partir de corpus *parallèles*
* extraction de lexiques bilingues à partir de corpus *comparables*
* la notion de comparabilité :
 * peu comparable
 * très comparable
 * parallèle



## Mesure de la comparabilité
Proposition d'une mesure de comparabilité basée sur la prévision de trouver la traduction de chaque mot du corpus. La mesure est "très légère" et ne dépend pas de ressources complexes comme un système de traduction automatique.




## Amélioration de la qualité du corpus





## Extraction de lexique bilingue





## Expérimentations

#### Données

Plusieurs corpus (tokenisés, POS-taggés, lemmatisés) sont utilisés :
* corpus **parallèle** EN-FR _Europarl_
* TREC Associated Press (EN)
* CLEF (EN-FR)
* 2 corpus monolingues issus d'un dump de Wikipedia
  * 1 FR (378k docs)
  * 1 EN (368k docs)

Un dictionnaire biligue
* 33k mots EN
* 27k mots FR


#### Résultats



![alt text][fig1]









[fig1]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/LiGaussierFig1.png "Résultats"
