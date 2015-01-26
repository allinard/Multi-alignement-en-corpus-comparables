# Résumé de l'article : Looking at Unbalanced Specialized Comparable Corpora for Bilingual Lexicon Extraction
---------

### En quelques mots : 
Ces travaux se penchent sur la qualité des lexiques biligues extraits à partir de corpus comparables déséquilibrés


## Introduction
L'article veut montrer que des corpus comparables pour l'extraction de lexiques bilingues ne doivent pas nécessairement être équilibrés, dans le cas de domaines spécialisés notamment



## Etat de l'art

#### Approche standard
Se base sur le fait qu'un mot et sa traduction tendent à apparaitre dans les mêmes contextes lexicaux (identification des affinités de 1er ordre). Les étapes de cette approche sont :
* Calcul des vecteurs de contexte (calcul pour chaque mot de ses co-occurrents et du nombre de co-occurrences)
* Transfert des vecteurs de contexte
* Recherche des traductions candidates

Cette approche n'est pas censée être sensible à la taille des corpus dans la mesure ou les vecteurs de contexte sont calculés de façon cloisonnée (les vect. de ctxt. source d'une part, et les vect. de ctxt. cible d'autre part)


#### Modèle prédictif ([Hazem & Morin (2013)](http://www.aclweb.org/anthology/I13-1196))

Ré-estimation du comptage des co-occurrences avec une fonction de prédiction. Consiste à assigner à chaque co-occurrence observée d'un corpus comparable de petite taille la valeur apprise dans un grand corpus d'entrainement



#### Autres
* [Prochasson & al. (2009)]() : renforcement des mots du contexte qui sont des translitérations ou des mots composés scientifiques dans la langue cible
* [Ismail & Manandhar (2010)]() : filtrage du bruit dans les vecteurs de contexte en considérant les mots pertinents du domaine
* [Rubino & Linarès (2011)]() : amélioration des mots du contexte sur le fait qu'un mot et sa traduction partagent des similarités thématiques _(approche par thésaurus ???)_
* [Yu & Tsujii (2009)]() : remplacement de la méthode fenêtre par une méthode basée sur la syntaxe (amélioration de la représentation du contexte lexical)
* [Morin & Prochasson (2011)]() : combinaison d'un dictionnaire général et d'un dictionnaire spécialisé
* [Déjean & al. (2002)]() : utilisation d'un thésaurus spécialisé
* [Koehn & Knight (2002)]() : utilisation de cognats et de contextes similaires
* [Bouamor & al. (2013)]() : désambiguïsation dans la langue cible
* [Gaussier & al. (2004)]() : désambiguïsation dans la langue source et la langue cible en utilisant Canonical Correlation Analysis et Probabilistic Latent Semantic Analysis
* [Chiao & Zweigenbaum (2002)]() : distibution symétrique des mots
* [Laroche & Langlais (2010)]() : similarité graphique entre les termes source et cible




## Expérimentations 
Les ressources sont les suivantes :
* Deux corpus, tokenisés, POS-taggés et lemmatisés par TermSuite 
  * Corpus sur le cancer du sein (530k mots FR - 7.4M mots EN divisé en 14 parties de 530k mots chacune)
  * Corpus sur le diabète (257k mots FR - 3.5M mots EN divisé en 14 parties de 250k mots chacune)
* Dictionnaire FR-EN généraliste ELRA
* Listes de référence terminologiques du méta-thésaurus UMLS
  * 169 fr/en mots simples pour le cancer du sein
  * 244 fr/en mots simples pour le diabète


#### Evaluation de l'approche standard

![alt text][fig1]


#### Evaluation de l'approche prédictive

![alt text][fig2]


![alt text][fig3]


![alt text][fig4]





[fig1]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/MorinHazemFig1.png "MAP approche standard"
[fig2]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/MorinHazemFig2.png "MAP approche modèle de regression"
[fig3]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/MorinHazemFig3.png "Comparaison des modèles de regression"
[fig4]: https://github.com/allinard/Multi-alignement-en-corpus-comparables/blob/master/Articles/images/MorinHazemFig4.png "MAP approche standard avec la meilleure configuration"

