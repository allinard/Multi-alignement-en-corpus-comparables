# Elements sur l'extraction de lexiques bilingues à partir de corpus comparables (thèse de F. Sadat (2003))
---------

### En quelques mots : 
Il s'agit ici d'éléments de thèse sur l'extraction de lexiques bilingues


## Ce qui existe
L'approche avec corpus parallèles a été plus parcourue que celle avec corpus comparables. Parmi les approches avec corpus comparables :
* [Rapp (1999)](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.35.558&rep=rep1&type=pdf) obtient de bons résultats sur la paire EN-DE (89% top 10 - 100 mots - on ne sait pas si il s'agit de mots fréquents ou non)
* [Peter & Picchi (1995)](http://link.springer.com/chapter/10.1007/978-1-4615-5661-9_7) démontrent avec des expérimentations sur EN-IT l'importance de la qualité des ressources linguistiques telles que le dictionnaire bilingue ou bien l'analyseur morpho-syntaxique
* [Tanaka & Iwasaki (1996)](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.47.1150&rep=rep1&type=pdf) alignement bilingue de coocurrences de mots pour extraire des paires "mot-traduction" de corpus comparables non alignés
* [Dagan & Itai (1994)](http://www.cs.technion.ac.il/~itai/publications/CL/DI.pdf) alignement des cas de co-occurrence du corpus de la langue source avec des co-occurrence statistiquement extraites de celui de la langue cible
* [Nakagawa (2000)](http://www.mt-archive.info/LREC-2000-Nakagawa.pdf) méthode de désambiguïsation de mots japonais pour une traduction en anglais. Repose fortement sur des dictionnaires bilingues
* [Koehn & Knight (2002)](http://homepages.inf.ed.ac.uk/pkoehn/publications/learnlex2002.pdf) méthode combinée avec des cognats, contextes similaires, similarité et fréquence des mots à base d'un lexique DE-EN (noms seulements)



## Extraction de lexiques bilingues à partir de corpus comparables et de thésaurus multilingue

Article de [Sadat, Déjean & Gaussier (2002)](http://acl-arc.comp.nus.edu.sg/archives/acl-arc-090501d3/data/pdf/anthology-PDF/C/C02/C02-1166.pdf)

L'idée à la base, dans l'extraction de lexiques bilingues à partir de corpus comparables est la suivante :
* On se base sur le principe des collocations similaires, c'est-à-dire qu'on considère que si deux mots sont des traductions mutuelles, alors leurs colloquants les plus fréquents seront, entre eux, des traductions mutuelles possible.
* ...c'est pourquoi on calcule les vecteurs de contexte source et les vecteurs de contexte cible des mots du corpus en langue source et ceux du corpus en langue cible
* On traduit ensuite les vecteurs de contexte grace à un dictionnaire bilingue LS-LC
* On calcule la similarité (cosinus) de chaque mot source avec chaque mot cible
* On normalise les probabilités et on obtient des traductions candidates

Les thésaurus (liste organisée de termes représentant les concepts d'un domaine) multilingues établissent un rapprochement entre plusieurs langues grâce aux correspondances mulilingues entre des classes de concept. Une classe de concept dans le thésaurus lie des noms alternatifs d'un même concept ensemble.

TODO

Voici le schéma résultant du modèle de traduction hybride impliquant l'utilisation de corpus comparables, de thésaurus multilingue et de dictionnaire bilingue :

![alt text][fig1]





## Améliorations pour l'acquisition de terminologie bilingue

TODO - CLIR

TODO - Schéma CLIR






[fig1]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/sadat1.png "Structure générale de la méthode proposée"
