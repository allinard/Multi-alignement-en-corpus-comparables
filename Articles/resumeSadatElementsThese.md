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


#### Approche standard (l'existant)

L'idée à la base, dans l'extraction de lexiques bilingues à partir de corpus comparables est la suivante :
* On se base sur le principe des collocations similaires, c'est-à-dire qu'on considère que si deux mots sont des traductions mutuelles, alors leurs colloquants les plus fréquents seront, entre eux, des traductions mutuelles possible.
* ...c'est pourquoi on calcule les vecteurs de contexte source et les vecteurs de contexte cible des mots du corpus en langue source et ceux du corpus en langue cible
* On traduit ensuite les vecteurs de contexte grace à un dictionnaire bilingue LS-LC
* On calcule la similarité (cosinus) de chaque mot source avec chaque mot cible
* On normalise les probabilités et on obtient des traductions candidates


#### Approche thésaurus multilingue

Les thésaurus (liste organisée de termes représentant les concepts d'un domaine) multilingues établissent un rapprochement entre plusieurs langues grâce aux correspondances mulilingues entre des classes de concept. Une classe de concept dans le thésaurus lie des noms alternatifs d'un même concept ensemble.

Dans notre cas, le thésaurus peut aider en trouvant des correspondances entre les classes de concept entre les langues afin de sélectionner la meilleure traduction d'un mot. Le protocole proposé est donc le suivant :
* Pour chaque mot source, et pour chaque mot cible, on calcule la probabilité de la classe de concept du mot source et la probabilité du mot cible selon cette même classe de concept
  * pour cela on recourt aux vecteurs de contexte (car si un mot du corpus est similaire à un terme présent dans la classe de concept, alors ils ont de fortes chances de partager le même contexte et d'avoir des vecteurs de contexte proches)
  * pour calculer le vecteur de contexte d'une classe de concept, on fait la somme des vecteurs de contexte de tous les termes de la classe. Ainsi, on arrive à determiner la similarité entre un mot et un concept en calculant la similarité (cosinus).
* Pour chaque paire de mot (LS-LC), on sélectionne les classes de concept à utiliser
  * soit en prenant en compte toutes les classes de concept du thésaurus
  * soit en prenant les n meilleures classes maximisant le produit de la proba de la classe de concept du mot source et de la proba du mot cible d'appartenir à la classe de concept
  * soit en prenant le concept parent dans le cas ou un mot possède plusieurs classes de concept et ou ces classes sont liées
* On calcule la probabilité de la traduction en LC d'un mot en LS d'après les classes de concept sélectionnées (pour cela on fait la somme, pour toutes les classes de concept sélectionnées, du produit de la proba de la classe de concept du mot source et de la proba du mot cible d'appartenir à la classe de concept)

#### Combinaison de différents modèles de traduction

Ces modèles sont combinés, puisque pour une traduction donnée la probabilité est la moyenne des résultats donnés par :
* Approche standard
* Approche thésaurus multilingue



#### Schéma

Voici le schéma résultant du modèle de traduction hybride proposé par Sadat, impliquant l'utilisation de corpus comparables, de thésaurus multilingue et de dictionnaire bilingue :

![alt text][fig1]



#### Expérimentations

Ressources :
* [MuchMore corpus](http://muchmore.dfki.de/resources1.htm) composé de 5500 résumés d'articles médicaux en DE-EN
* [POS-tagger XEROS](https://open.xerox.com/Services/fst-nlp-tools/Consume/Part%20of%20Speech%20Tagging%20%28Standard%29-178)
* Dictionnaire DE-EN (50000 entrées et 149338 mots)
* Thésaurus [MeSH (EN)](http://www.nlm.nih.gov/mesh/meshhome.html) et son équivalent, [DMD (DE)](http://www.nlm.nih.gov/research/umls/)

Les résultats (F-score) sont au mieux de
* **75.4** au top5 et **83.2** au top10 dans le cas de prendre les n meilleures classes de concept du thésaurus maximisant la probabilité de la traduction
* **77.3** au top5 et **84.1** au top10 dans le cas de prendre les 20 concepts parents du thésaurus et pour un mot donné dans le cas ou un mot possède plusieurs classes de concept et ou ces classes sont liées








## Améliorations pour l'acquisition de terminologie bilingue

Structure du modèle de traduction en 2 étapes basé sur des corpus comparables (CLIR) :

![alt text][fig2]


Conception globale du modèle proposé pour l'acquisition de terminologie bilingue à partir de corpus comparables (CLIR) :

![alt text][fig3]






#### Expérimentations

Précision et Rappel des modèles de traduction avec corpus comparables et élagage basé sur la linguistique : 

![alt text][fig4]

Précision et Rappel des modèles de traduction avec corpus comparables, élagage basé sur la linguistique, et combinaisons linéaires améliorées avec élagage basé sur la linguistique : 
![alt text][fig5]






[fig1]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/sadat1.png "Structure générale du modèle de traduction hybride (corpus comparables - dictionnaire bilingue - thésaurus multilingue)"
[fig2]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/sadat2.png "Structure du modèle de traduction en 2 étapes basé sur des corpus comparables (CLIR)"
[fig3]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/sadat3.png "Conception globale du modèle proposé pour l'acquisition de terminologie bilingue à partir de corpus comparables (CLIR)"
[fig4]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/sadat4.png "P/R des modèles de traduction avec corpus comparables et élagage basé sur la linguistique"
[fig5]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/sadat5.png "P/R des modèles de traduction avec corpus comparables, élagage basé sur la linguistique, et combinaisons linéaires améliorées avec élagage basé sur la linguistique"
