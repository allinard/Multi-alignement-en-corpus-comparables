# Résumé de l'article : [Extended pivot-based approach for bilingual lexicon extraction](http://www.researchgate.net/profile/Hyeongwon_Seo/publication/268049712_Extended_pivot-based_approach_for_bilingual_lexicon_extraction/links/546073450cf27487b450c275.pdf)
---------

### En quelques mots : 
Cet article traite de extension de l'approche par pivot pour l'extraction de lexiques bilingues dans le cas de paires de langues dont on dispose de peu de ressources.



## Intro
En gros, l'approche globale voulue est la suivante :

1. Calcul de vecteurs de contexte entre la langue source et une langue pivot (souvent, l'anglais), et la langue cible et la langue pivot
2. Identification des vecteurs de contexte similaires dans la langue source (dans le but d'améliorer les résultats retournés pour les mots polysémiques)
3. Extraction des traductions candidates à partir des vecteurs de contexte cible par la similarité entre les vecteurs de contexte source et cible

Les expérimentations sont faites avec des *corpus parallèles*. Cependant, je pense qu'on peut adapter la méthode à des corpus *comparables*.


## Etat de l'art

Ce qui existe dans le domaine :

* Représentation des mots par un vecteur de contexte basé sur leur contexte lexical ([Fung & McKeown (1997)](http://www.cs.columbia.edu/nlp/papers/1997/fung_mckeown_97.pdf) ; [Cao & Li (2002)](http://research.microsoft.com/en-us/people/hangli/cao-li-coling02.pdf?origin=publication_detail)
* Dictionnaire bilingue pour traduire les vecteurs de contexte ([Koehn & Knight (2002)](http://homepages.inf.ed.ac.uk/pkoehn/publications/learnlex2002.pdf) ; [Koehn, Och & Marcu (2003)](http://www.dtic.mil/dtic/tr/fulltext/u2/a461156.pdf))
* Mots similaires partageant des contextes lexicaux ([Déjean, Sadat & Gaussier (2002)](http://acl-arc.comp.nus.edu.sg/archives/acl-arc-090501d3/data/pdf/anthology-PDF/C/C02/C02-1166.pdf))
* Approche standard basée sur pivot ([Seo, Kwon & Kim (2013)](http://www.aclweb.org/anthology/W13-2502)) qui extrait des lexiques bilingues en utilisant une langue pivot (souvent : l'anglais)


Ce dont l'article s'inspire plus fortement sont les approches décrites ci-dessous (qui se basent toutes sur des approches basées sur le contexte de [Rapp (1999)](http://www.aclweb.org/anthology/P99-1067))

#### Approche standard basée sur un pivot (Kim Seo Kwon 2013 : [Bilingual Lexicon Extraction via Pivot Language and Word Alignment Tool](http://www.aclweb.org/anthology/W13-2502))

Un résumé est [ICI](https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/resumeKwoSeoKim13.md)

Pour extraire un lexique bilingue de paire de langues disposant de peu de ressources et SANS ressource externe (pas de dictionnaire bilingue) MAIS avec une langue pivot. 

Les étapes de la mise en place d'une telle méthode sont les suivantes :

* Calcul des vecteurs de contexte depuis 2 jeux de corpus *parallèles* (langue source - langue pivot et langue pivot - langue cible)
* Calcul de la similarité entre les vecteur de contexte source et les vecteurs de contexte cible.
* Renvoi des traductions candidates d'après les scores de similarité.



#### Approche étendue basée sur le contexte ([Déjean Sadat & Gaussier 2002](http://acl-arc.comp.nus.edu.sg/archives/acl-arc-090501d3/data/pdf/anthology-PDF/C/C02/C02-1166.pdf))

Le but de cette approche est d'avoir une dépendance moindre vis à vis de la couverture du dictionnaire bilingue initial. On utilise aussi les affinités du second ordre de la langue source (les mots qui partagent les mêmes environnements). L'idée est la suivante :

* les k plus proches mots dans le texte source sont identifiés
* ils sont ensuite traduits dans la langue cible avec le dictionnaire bilingue
* le score de similarité de chaque mot dans la langue cible est calculé







## L'approche en détails

Ce qui est proposé dans l'article est l'[approche basée sur un pivot](https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/resumeKwoSeoKim13.md) _étendue_. Pour cela :

* On construit des vecteurs de contexte (entre LS et LS, LS et LP, LP et LC) en utilisant la *Pointwise Mutual Information* (PMI - quantifie l'écart entre la probabilité de la coïncidence d'une paire de résultats donné par leur distribution conjointe et leurs distributions individuelles, en supposant l'indépendance)
* On calcule les k plus proches mots (en utilisant le vect. ctxt. LS-LS)
* A partir des vect. ctxt. LS-LP et des k plus proches mots, on calcule les vect. ctxt. des k plus proches mots LS-LP
* A partir des vect. ctxt. LP-LC et des vect. ctxt. des kppm LS-LP, on calcule la similarité de tous les scores de similarité possibles partageant des kppm entre les mots de LS et ceux de LC. On obtient donc des traductions candidates qui sont évaluées, triées puis retournées

Voici un schéma récapitulatif :

![alt text][fig1]



## Expérimentations

Conditions similaires à [l'approche standard basée sur un pivot](https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/resumeKwoSeoKim13.md)

* corpus *parallèle* KR-EN, tokenisé, étiqueté morpho-syntaxiquement, et sans mots outils 
* corpus *parallèle* EUROPARL pour EN-FR, tokenisé, étiqueté morpho-syntaxiquement, et sans mots outils

Pour l'évaluation, lexique bilingue pour le KR-FR, contenant 100 mots fréquents et 100 mots rares (HIGH et LOW respectivement dans les résultats présentés)

Les métriques sont : 
* exactitude
* MRR (Mean Reciprocal Recall), prend plus en compte les traductions données à un rang élevé
* Rappel : RR (Rated Recall), prend en compte l'importance des traductions (le nombre de fois qu'elles apparaissent dans le document)

#### Résultats 

Voici les résultats (la langue pivot est l'anglais - les résultats sont la moyenne des 2 cas "FR->KR" et "KR->FR") :

Premièrement (LOW en haut et HIGH en bas), 

![alt text][fig2]

Secondement (LOW en haut et HIGH en bas), 

![alt text][fig3]

Enfin, comparaison des résultats entre méthode standard et méthode étendue

![alt text][fig4]





## Avec des corpus comparables

Utiliser un dictionnaire LS-LP et LP-LC pour la construction de vecteurs de contexte LS traduits en LP puis LC traduits en LP ?




[fig1]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/SeoKwonKim14Fig1.png "Structure générale de la méthode proposée"
[fig2]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/SeoKwonKim14Fig2.png "Exactitude de la méthode proposée"
[fig3]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/SeoKwonKim14Fig3.png "MRR de la méthode proposée"
[fig4]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/SeoKwonKim14Fig4.png "Comparaison des résultats entre méthode standard et méthode étendue"
