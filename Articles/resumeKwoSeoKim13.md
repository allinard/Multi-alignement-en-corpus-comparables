# Résumé de l'article : [Bilingual Lexicon Extraction via Pivot Language and Word Alignment Tool](http://www.aclweb.org/anthology/W13-2502)
---------

### En quelques mots : 
Cet article traite de l'approche par pivot pour l'extraction de lexiques bilingues dans le cas de paires de langues dont on dispose de peu de ressources.


## Intro
Il s'agit ici de proposer une méthode pour l'extraction de lexiques bilingues en utilisant une langue pivot (pour la représentation des vecteurs de contexte de la langue source et ceux de la langue cible) et de la recherche d'information (pour calculer la similarité entre les vecteurs de contexte de la langue source et ceux de la langue cible). 





## Etat de l'art
Ils se basent sur différents travaux :
* Une façon directe pour l'extraction de lexique bilingue et l'alignement de mots dans un corpus parallèle ([Lu & Xia (1994)](http://info.cse.ust.hk/~dekai/library/WU_Dekai/amta94.Wu_Xia.ps))
* Extraction de lexique bilingue à partir de corpus comparables ([Fung (1995)](http://academiccommons.columbia.edu/download/fedora_content/download/ac:159888/CONTENT/fung_95a.pdf),[Yu & Tsujii (2009)](http://www.mt-archive.info/MTS-2009-Yu.pdf),[Ismail & Manandhar (2010)](http://www.aclweb.org/anthology/C/C10/C10-2055.pdf))
* L'utilisation d'une langue pivot ([Tanaka & Umemura (1994)](http://dl.acm.org/citation.cfm?id=991937), [Wu & Wang (2007)](http://link.springer.com/article/10.1007/s10590-008-9041-6#page-1), [Tsunakawa & al. (2008)](http://www.mt-archive.info/LREC-2008-Tsunakawa.pdf))
* Extraction de lexiques bilingues par de la recherche d'information ([Fung (1998)](http://link.springer.com/chapter/10.1007/3-540-49478-2_1#page-2), [Gaussier & al. (2004)](http://dl.acm.org/citation.cfm?id=1219022), [Hazem & al. (2012)](http://lrec.elra.info/proceedings/lrec2012/pdf/784_Paper.pdf))




## Approche proposée

Ils utilisent des corpus *parallèles*. Cependant, la technique décrite serait applicable à des corpus comparables. Leur choix s'explique par le fait que l'alignement de corpus parallèle est plus précis, et qu'ils n'ont pas besoin d'utiliser de dictionnaire bilingue pour la traduction de vecteurs de contextes.

La démarche est la suivante (LS=langue source; LP=langue pivot; LC=langue cible) :
* A partir du corpus parallèle LS-LP, on réalise un alignement entre les mots du corpus LS et celui LP. Pour cela, on utilise [_Anymalign_](http://anymalign.limsi.fr/), un aligneur multi-lingue sous-phrastique. On obtient donc les vecteurs de contexte LS-LP (les mots sont pondérés par _Anymalign_)
* A partir du corpus parallèle LP-LC, on réalise un alignement entre les mots du corpus LP et celui LC (toujours avec _Anymalign_). On obtient les vecteurs de contexte LP-LC
* On calcule la similarité entre chaque mot du vecteur de contexte source (LS-LP) et tous les mots du vecteur de contexte cible cible (LP-LC) : on utilise la similarité cosinus
* Les résultats sont triés et retournés en fonction des scores de similarité

L'avantage d'une telle méthode (et d'utiliser des corpus parallèles) est qu'on se passe des dictionnaires bilingues LS-LP et LP-LC.

Voici un schéma récapitulatif :

![alt text][fig1]



## Expérimentations

Utilisation d'Anymalign.

Corpus KR-EN de Seo et al. (2006)

Corpus EN-ES et EN-FR de Europarl

Les mots sont tokenisées par Hannanum pour le KR, Tree-Tagger pour EN ES et FR

Pour l'évaluation, deux lexiques bilingues unidirectionnels sont construits [à la main](http://dic.anver.com) pour le KR-ES et KR-FR, contenant chacun 100 mots fréquents et 100 mots rares

Métriques :
* exactitude
* rappel
* MRR (Mean Reciprocal Rank) : la moyenne des rangs réciproques des candidats de la traduction qui sont des traductions correctes pour un échantillon de mots

Voici les résultats

![alt text][fig2]

![alt text][fig3]





## Et si on faisait avec des corpus parallèles ?!

Le problème d'_Anymalign_ est de faire de l'alignement de corpus *parallèles*. On serait donc obligé de s'en passer si on travaillait avec des corpus *comparables*. Dans le cas de corpus comparables, on pourrait (idées) :
* Utiliser un dictionnaire LS-LP et LP-LC pour la construction de vecteurs de contexte LS traduits en LP puis LC traduits en LP
* Réaliser un alignement phrastique pour des corpus multilingues comparables
* _"autre chose"_ (à voir...)





[fig1]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/tree/master/Articles/images/Fig1.png "Structure générale de la méthode proposée"
[fig2]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/tree/master/Articles/images/Fig2.png "Exactitude de la méthode proposée"
[fig3]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/tree/master/Articles/images/Fig3.png "MRR de la méthode proposée"
