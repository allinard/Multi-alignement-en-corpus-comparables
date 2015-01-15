# Résumé de l'article : Extended pivot-based approach for bilingual lexicon extraction
---------

### En quelques mots : 
Cet article traite de extension de l'approche par pivot de l'extraction de lexiques bilingues dans le cas de paires de langues dont on dispose peu de ressources.



## Intro
On voit tout d'abord l'approche globale voulue :

1. Calcul de vecteurs de contexte entre la langue source et une langue pivot (souvent, l'anglais), et la langue cible et la même langue pivot
2. Identification des vecteurs de contexte similaires dans la langue source (dans le but d'améliorer les résultats retournés pour les mots polysémiques)
3. Extraction des traductions candidates à partir des vecteurs de contexte cible par la similarité entre les vecteurs de contexte source et cible


## Etat de l'art

Ce qui existe dans le domaine :

* Représentation des mots par un vecteur de contexte basé sur leur contexte lexical (Fung & McKeown 97 ; Cao & Li 02)
* Dictionnaire bilingue pour traduire les vecteurs de contexte (Koehn & Knight 02 ; Koehn Och & Knight 03)
* Mots similaires partageant des contextes lexicaux (Déjean Sadat & Gaussier 02)
* Approche standard basées sur pivot (Seo Kwon & Kim 13) qui est utile seulement pour les paires de langues pauvres en ressources, et qui extrait de lexiques bilingues en utilisant une langue pivot (comme l'anglais)


Ce dont l'article s'inspire plus fortement sont les approches décrites ci-dessous. Elles se basent toutes sur des approches basées sur le contexte (Rapp 99)

### Approche standard basée sur un pivot (Kim Seo Kwon 13)

Pour extraire un lexique bilingue de paire de langues disposant de peu de ressources et SANS ressource externe (ni dictionnaire bilingue, ni corpus parallèle). Utilise par contre une langue pivot. Du coup la dimension des deux vecteurs de contexte devient la même, il sont donc comparables et on n'a pas besoin d'un dictionnaire bilingue pour la phase de traduction.

Les étapes de la mise en place d'une telle méthode sont les suivantes :

* Calcul des vecteurs de contexte depuis 2 jeux de corpus parallèles (langue source - langue pivot et langue pivot - langue source)
* Calcul de la similarité entre le vecteur de contexte source et tous les vecteurs de contexte cible.
* Renvoi des traductions candidates d'après les scores de similarité.



### Approche étendue basée sur le contexte (Déjean Sadat & Gaussier 02)

Le but de cette approche est une dépendance moindre pour la couverture sur le dictionnaire bilingue initial. On utilise aussi les affinités du second ordre de la langue source (les mots qui partagent les mêmes environnements). L'idée est la suivante :

* les k plus proches mots dans le texte source sont identifiés
* le score de similarité de chaque mot dans la langue cible est calculé







## L'approche en détails

L'approche reprend celle basée sur le contexte étendue (Déjean Sadat & Gaussier 02). L'idée est de trouver les k plus proches mots dans le texte source et de mieux identifier les traductions candidates. Pour cela, les k plus proches mots du corpus source doivent être traduits dans la langue cible avec un dictionnaire bilingue : on a donc tous les mots représentés en langue source et les vecteurs de contexte de même dimensions.

D'un autre côté l'approche standard basée sur un pivot (Kim Seo Kwon 13) utilise une langue pivot connectant la langue source et la langue cible ce qui simplifie les calculs de similarité.

Ce qui est proposé dans l'article est une approche étendue basée sur un pivot. Pour cela :

* On construit des vecteurs de contexte (entre LS et LS, LS et LP, LP et LC) en utilisant la *Pointwise Mutual Information* (PMI - quantifie l'écart entre la probabilité de la coïncidence d'une paire de résultats donné par leur distribution conjointe et leurs distributions individuelles, en supposant l'indépendance)
* On calcule les k plus proches mots (en utilisant le vect. ctxt. LS-LS)
* A partir des vect. ctxt. LS-LP et des k plus proches mots, on calcule les vect. ctxt. des k plus proches mots LS-LP
* A partir des vect. ctxt. LS-LP, des vect. ctxt. LP-LC
* A partir des vect. ctxt. LP-LC et des vect. ctxt. des kppm LS-LP, on calcule la similarité de tous les scores de similarité possibles partageant des kppm entre les mots de LS et ceux de LC. On obtient donc des traductions candidates qui sont évaluées, triées puis retournées





## Expérimentations

* corpus parallèle KR-EN
* corpus parallèle EUROPARL pour EN-FR
* Accuracy : MRR (Mean Reciprocal Recall), prend plus en compte les traductions données à un rang élevé
* Rappel : RR (Rated Recall), prend en compte l'importance des traductions (le nombre de fois qu'elles apparaissent dans le document)



