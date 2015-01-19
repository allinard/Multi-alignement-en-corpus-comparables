# Résumé de l'article : [Bilingual Lexicon Extraction via Pivot Language and Word Alignment Tool](http://www.aclweb.org/anthology/W13-2502)
---------

### En quelques mots : 
Cet article traite de l'approche par pivot pour l'extraction de lexiques bilingues dans le cas de paires de langues dont on dispose de peu de ressources.


## Intro
Il s'agit ici de proposer une méthode pour l'extraction de lexiques bilingues en utilisant une langue pivot (pour la représentation des vecteurs de contexte de la langue source et ceux de la langue cible) et de la recherche d'information (pour calculer la similarité entre les vecteurs de contexte de la langue source et ceux de la langue cible). 





## Etat de l'art
Ils se basent sur différents travaux :
* A
* B
* C
* D




## Approche proposée

Ils utilisent des corpus *parallèles*. Cependant, la technique décrite serait applicable à des corpus comparables. Leur choix s'explique par le fait que l'alignement de corpus parallèle est plus précis.

La démarche est la suivante (LS=langue source; LP=langue pivot; LC=langue cible) :
* A partir du corpus parallèle LS-LP, on réalise un alignement entre les mots du corpus LS et celui LP. Pour cela, on utilise [_Anymalign_](http://anymalign.limsi.fr/), un aligneur multi-lingue sous-phrastique. On obtient donc les vecteurs de contexte LS-LP (les mots sont pondérés par _Anymalign_)
* A partir du corpus parallèle LP-LC, on réalise un alignement entre les mots du corpus LP et celui LC (toujours avec _Anymalign_). On obtient les vecteurs de contexte LP-LC
* On calcule la similarité entre chaque mot du vecteur de contexte source (LS-LP) et tous les mots du vecteur de contexte cible cible (LP-LC) : on utilise la similarité cosinus
* Les résultats sont triés et retournés en fonction des scores de similarité

L'avantage d'une telle méthode (et d'utiliser des corpus parallèles) est qu'on se passe des dictionnaires bilingues LS-LP et LP-LC.



## Expérimentations

Utilisation d'Anymalign.

Corpus KR-EN de Seo et al. (2006)

Corpus EN-ES et EN-FR de Europarl

Les mots sont tokenisées par Hannanum pour le KR, Tree-Tagger pour EN ES et FR

Pour l'évaluation, deux lexiques bilingues unidirectionnels sont construits [à la main](http://dic.anver.com) pour le KR-ES et KR-FR, contenant chacun 100 mots fréquents et 100 mots rares

Métriques :
* accuracy
* recall
* MRR (Mean Reciprocal Rank)


## Et si on faisait avec des corpus parallèles ?!

Le problème d'_Anymalign_ est de faire de l'alignement de corpus *parallèles*. On serait donc obligé de s'en passer si on travaillait avec des corpus *comparables*. Dans le cas de corpus comparables, on pourrait (idées) :
* Utiliser un dictionnaire LS-LP et LP-LC pour la construction de vecteurs de contexte LS traduits en LP puis LC traduits en LP
* Réaliser un alignement phrastique pour des corpus multilingues comparables
* _"autre chose"_ (à voir...)
