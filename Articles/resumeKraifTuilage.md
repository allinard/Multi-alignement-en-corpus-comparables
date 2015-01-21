# Tuilage des couples de langues (Kraif)
---------

### En quelques mots : 
Définition du tuilage d'alignements. Il s'agit dans notre cas d'une aide à la définition d'une langue pivot. Il s'agit dans les travaux de _Kraif_ de corpus *parallèles*.


## Contexte
Kraif fait l'état des lieux et des expérimentations sur l'alignement de corpus _multi-parallèles_, c'est à dire plusieurs corpus *parallèles* impliquant plus de 2 langues.


## Etat de l'art 
L'existant :
* Hypothèse de la triangulation multilingue, idée selon laquelle un jeu de plus de 2 langues dans le cadre de textes parallèles peut apporter encore plus d'information, et peut servir à la désambiguïsation lexicale, [Dagan et al. (1991)](http://u.cs.biu.ac.il/~dagan/publications/TwoLanguages_P91-1017.pdf)
* Expérimentations du projet _Carmel_ par [Chen et al. (2005)](http://www.atala.org/taln_archives/TALN/TALN-2005/taln-2005-court-006.pdf) et [Kraif et al. (2006)]()
* Aligneur _MulItAl_ (Multilingual Iterative Aligner)
* Aligneur _JAM_ (Just An Aligner)


## L'idée principale
Est défini comme tuilage l'ensemble minimal de couples de langues tel que :
* chaque langue apparaît au moins dans 1 couple
* chaque couple possède au moins une langue en commun avec un autre couple
C'est grosso modo la définition de l'utilisation d'une langue pivot.

Parmi les tuilages possibles, celui qui est particulièrement recherché est celui qui met en jeu les couples les plus fortement associés (mettant en jeu des langues proches _génétiquement_)

L'idée est que les couples formés peuvent s'appuyer les uns sur les autres, de manière complémentaire, le tout pour former un tout plus solide.


## Expérimentations
Corpus multi-parallèle _Europarl_ en 10 langues (DA, DE, EN, ES, FI, FR, IT, NL, PT, SV)

D'après les données, et en calculant les langues les plus associées, les combinaisons de langues simples prenant l'anglais comme pivot sont, par ordre décroissant de force d'association : *EN-FR*, EN-IT, *EN-ES*, EN-PT, EN-SV, DA-EN, EN-NL, *DE-EN* etc...

Pour les couples de langues qui nous intéressent (FR-EN-DE-ES) les résultats en utilisant l'anglais comme langue pivot sont :
* DE-FR : P=0.95 R=0.79
* ES-FR : P=0.97 R=0.81
