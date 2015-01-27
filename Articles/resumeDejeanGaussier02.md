# Résumé de l'article : [Une nouvelle approche à l'extraction de lexiques bilingues à partir de corpus comparables](http://lexicometrica.univ-paris3.fr/thema/thema6/Dejean.pdf)
---------

### En quelques mots : 
Il est question ici d'une nouvelle approche à l'extraction de lexiques bilingues à partir de corpus comparables.

## Intro

#### Définition d'un corpus comparable (une bonne citation pour le mémoire !!!) :

Deux corpus de deux langues l1 et l2 sont dits comparables s'il existe une sous-partie non négligeable du vocabulaire du corpus de langue l1, respectivement l2, dont la traduction se trouve dans le corpus de langue l2, respectivement l1


#### "Sous-partie non négligeable" ?

* Même domaine
* Même période





## Sémantique distributionnelle et corpus comparables

Hypothèses existantes :
* si deux mots ont des distributions similaires, alors ils sont reliés sémantiquement
* les mots dont les distributions sont les plus similaires à celle d'un mot donné sont, avec une forte probabilité, sémantiquement reliés à ce mot
* les mots de la langue l1 dont les distributions normalisées sont les plus similaires à la distribution d'un mot donné de la langue l2 sont, avec une forte probabilité, traduction de ce mot
* deux mots de l1 et l2 sont, avec une forte probabilité, traduction l'un de l'autre si leurs similarités avec les entrées des ressources bilingues disponibles sont proches




## Extraction de lexique bilingue

#### Approche directe
* pour chaque mot, construction du vecteur de contexte (dans une fenêtre de n phrases autour de la phrase contenant le mot (en gal. n=1) avec une pondération de type information mutuelle)
* les vecteurs de ctxt. des mots de l1 sont traduits en l2 avec un dictionnaire bilingue
* comparaison des vect. ctxt. l1 et l2 (similarité cosinus)
* normalisation des valeurs de similarité et renvoi des traductions candidates

#### Approche par similarité interlangue
Basé sur l'hypothèse "deux mots de l1 et l2 sont, avec une forte probabilité, traduction l'un de l'autre si leurs similarités avec les entrées des ressources bilingues disponibles sont proches"

Deux approches :
* plate : pas de structure
* hiérarchique : utilise la structure du thésaurus


## Expérimentations

#### Données
* Deux corpus EN-DE segmentés (DE), lemmatisés et étiquetés :
  * Corpus _MUCHMORE_ **parallèle _bruité_** EN-DE de 845 résumés d'articles scientifiques sur la chirurgie provenant de la base de données MEDLINE
  * Corpus _GIRT_ de CLEF2002 constitué de 86k articles DE et équivalent en EN
* Dictionnaire ELRA EN-DE
* Méta-thésaurus UMLS comprenant 2 thésaurus allignés :
  * Thésaurus EN du MeSH
  * Thésaurus DE du DMD
* lexique de référence extrait manuellement
  * _MUCHMORE_ : 1800 mots
  * _GIRT_ : 180 mots



#### Résultats

Evalution P, R, F, sur le TOP1..20

Méthode standard (traduction des vecteurs de contexte) - Corpus médical

![alt text][fig1]




Méthode plate - Corpus médical (évaluation en fonction du nombre d'entrées considérées)

![alt text][fig2]




Méthode hiérarchique (évaluation en fonction du nombre d'entrées)

![alt text][fig3]





Evaluation méthode plate/standard - Corpus GIRT

![alt text][fig4]





Combinaison de la méthode standard et des nouvelles méthodes proposées - Corpus médical

![alt text][fig5]







[fig1]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/DejeanGaussierFig1.png "Méthode standard (traduction des vecteurs de contexte) - Corpus médical"
[fig2]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/DejeanGaussierFig2.png "Méthode plate - Corpus médical (évaluation en fonction du nombre d'entrées considérées)"
[fig3]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/DejeanGaussierFig3.png "Méthode hiérarchique (évaluation en fonction du nombre d'entrées)"
[fig4]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/DejeanGaussierFig4.png "Evaluation méthode plate/standard - Corpus GIRT"
[fig5]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/DejeanGaussierFig5.png "Combinaison de la méthode standard et des nouvelles méthodes proposées - Corpus médical"
