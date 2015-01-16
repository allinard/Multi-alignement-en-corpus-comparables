# Résumé de l'article : Statistical Multi-Source Translation
---------

### En quelques mots : 
Il s'agit ici de la proposition de méthodes permettant de traduire un texte donné en plusieurs langues source en une seule langue cible.

## Introduction
A priori, les avantage d'une telle technique seraient :

* Meilleure désambiguisation des mots : souvent les ambiguités n'existent que dans 2 paires de langues, mais pas dans d'autres
* Meilleur réordonnement des mots : l'ordre des mots de langues proche est similaire, et on espère que dans le lot des langues sources on a des langues similaires
* Pas besoin de résoudre les anaphores : on espère que dans les langues sources les pronoms sont déjà traduits correctement
* 


## Etat de l'art : traduction statistique

* Pour une phrase donnée en langue source, on va choisir, parmi les phrases en langue cible celle qui est la plus probable
* on utilise un modèle de langage de la langue cible
* un modèle de traduction par phrase



## Traduction multi-source statistique

Pour 1 document donné en N langues :

* Alignement de segments (dans les expérimentations = paragraphes) en utilisant Gale & Church 93 disant que deux paragraphes sont alignables si elles ont grosso modo la même longueur (heuristique de la longueur). On a donc N-1 corpus bilingues alignés au grain paragraphe.
* On aligne ensuite au grain phrase avec la même méthode (heurisitique de la longueur) : on a donc N-1 corpus bilingues alignés au grain phrase.
* Filtrage de phrases avec un alignement suspect (1 longue avec une courte ou alignement de faible proba selon le HMM d'alignement)
* Pré-traitements

Ensuite, au choix, 2 méthodes :
* PROD
	** étant donné un mot cible, les mots source sont considérés comme statistiquement indépendants.
  ** on doit prendre en compte tous les mots cibles possible pour réaliser la maximisation (Och 99)
  ** on approxime que, pour chaque langue, la meilleure traduction d'un mot est calculée en prenant seulement en compte le modèle de traduction de cette langue
  ** on émet ensuite l'hypothèse qu'il y a autant de phrases cible que de langues à chercher, le tout dans un algorithme de recherche uni-source (Och 99)
* MAX 
	** on traduit en utilisant une des N langues source
  ** on choisit la traduction qui obtient le meilleur score


## Expérimentations

Utilisation du *Bulletin of the European Union*, disponible dans 11 langues, puis réalisation des méthodes ci-dessus.

Les mesures utilisée sont le WER et le PER (Position independant word Error Rate).

MAX améliore les résultats en comparaison à la traduction uni-source jusqu'à 3 langues sources utilisées

PROD améliore les résultats en comparaison à la traduction uni-source jusqu'à 6 langues sources utilisées



