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

La mesure de comparabilité est définie comme étant la base de l'espérance de trouver pour chaque mot en LS dans le vocabulaire LS sa traduction dans le vocabulaire LC. C'est en d'autres termes la proportions de mots LS traduits dans la partie en LS du corpus comparable.



## Amélioration de la qualité du corpus

L'amélioration de la qualité du corpus se définit en deux étapes :
* extraction de la sous-partie très comparable du corpus
* enrichissement de la sous-partie peu comparable du corpus


#### Extraction de la sous-partie très comparable du corpus

L'idée est d'extraire une sous-partie du corpus qui atteint un seuil comparabilité donné (pour avoir des corpus très comparables).

En effet, on peut extraire progressivement à partir d'un corpus bilingue une sous-partie avec un degré minimum de comparabilité en ajoutant de nouveaux éléments de manière itérative, à condition que les nouveaux éléments aient un degré de comparabilité suffisant et qu'ils soient moins comparables à la sous-partie actuellement extraite.

On a donc en sortie un corpus avec un degré de comparabilité élevé.




#### Enrichissement de la sous-partie peu comparable du corpus

La sous-partie peu comparable du corpus est ce qu'il reste du corpus initial lorsqu'on a extrait la sous-partie très comparable du corpus. L'idée ici est de l'enrichir en recourant à des ressources externes. Deux méthodes :
* extraire les mots les plus représentatifs des documents de la sous-partie peu comparable du corpus, les traduire avec un dict. bilingue, et récupérer des documents à partir de ces mots-clés
* utiliser des corpus comparables existants. Une fois un corpus comparable externe consitué, on récupère les paires de document très comparables à partir de la partie LS de la sous-partie peu comparable du corpus et de la partie LC du corpus externe. Ensuite, la partie LC de la sous-partie peu comparable du corpus est enrichie avec la partie LS du corpus externe (cf. algo article)





## Expérimentations sur l'extraction de lexiques bilingues

#### Données

Plusieurs corpus (tokenisés, POS-taggés, lemmatisés) sont utilisés :
* corpus **parallèle** EN-FR _Europarl_
* TREC Associated Press (EN)
* CLEF (EN-FR) qui inclut
 * GH95
 * LAT94
 * MON94
 * SDA94
 * SDA95
* 2 corpus monolingues issus d'un dump de Wikipedia
  * 1 FR (378k docs)
  * 1 EN (368k docs)

Un dictionnaire biligue
* 33k mots EN
* 27k mots FR


#### Résultats

Mesure de similarité améliorée : pour deux mots, poids fort si les mots apparaissent dans des paires de documents comparables plus souvent que la prédiction ; faible sinon.

Evaluation (au TOP20) suivant :
* la fréquence des mots :
 * mots dont la fréq. < 100 (WL)
 * mots dont la fréq. > 400 (WH)
 * mots 100 < fréq. < 400 (WM)
* les corpus :
 * corpus de base (C0), composé de GH95 et SDA95
 * la sous-partie très comparable de C0 qui est supérieureure à un certain degré de comparabilité (CH)
 * un corpus de la taille de CH constitué de documents issus de C0 choisis aléatoirement (C'H)
 * la sous-partie peu comparable de C0 enrichie avec LAT94 et MON94 (C1)
 * la sous-partie peu comparable de C0 enrichie avec Wiki-EN et Wiki-FR (C2)
 * C1 calculé avec la mesure de similarité améliorée (C1new)
 * C2 calculé avec la mesure de similarité améliorée (C2new)

![alt text][fig1]









[fig1]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/LiGaussierFig1.png "Résultats"
