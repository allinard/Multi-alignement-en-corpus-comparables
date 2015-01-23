# Résumé de l'article : Looking at Unbalanced Specialized Comparable Corpora for Bilingual Lexicon Extraction
---------

### En quelques mots : 
Ces travaux se penchent sur la qualité des lexiques biligues extraits à partir de corpus comparables déséquilibrés


## Introduction
L'article veut montrer que des corpus comparables pour l'extraction de lexiques bilingues ne doivent pas nécessairement être équilibrés, dans le cas de domaines spécialisés notamment



## Etat de l'art

#### Approche standard
Se base sur le fait qu'un mot et sa traduction tendent à apparaitre dans les mêmes contextes lexicaux (identification des affinités de 1er ordre). Les étapes de cette approche sont :
* Calcul des vecteurs de contexte (calcul pour chaque mot de ses co-occurrents et du nombre de co-occurrences)
* Transfert des vecteurs de contexte
* Recherche des traductions candidates

Cette approche n'est pas censée être sensible à la taille des corpus dans la mesure ou les vecteurs de contexte sont calculés de façon cloisonnée (les vect. de ctxt. source d'une part, et les vect. de ctxt. cible d'autre part)


#### Modèle prédictif ([Hazem & Morin (2013)](http://www.aclweb.org/anthology/I13-1196))

Ré-estimation du comptage des co-occurrences avec une fonction de prédiction. Consiste à assigner à chaque co-occurrence observée d'un corpus comparable de petite taille la valeur apprise dans un grand corpus d'entrainement



#### Autres
* [ ()]() :
* [ ()]() :
* [ ()]() :
* [ ()]() :
* [ ()]() :
* [ ()]() :
* [ ()]() :
* [ ()]() :
* [ ()]() :





## Expérimentations 
Les ressources sont les suivantes :
* A
* B
* C
* D
* E
* F


#### Evaluation de l'approche standard


#### Evaluation de l'approche prédictive





