# Résumé de l'article : [Towards Bilingual Term Extraction in Comparable Patents](http://www.aclweb.org/anthology/Y09-2038)
---------

### En quelques mots : 
Il s'agit ici d'étudier l'extraction de termes bilingues dans le cas de brevets. L'idée est d'exploiter la richesse de tels documents en termes techniques.


## Intro
Il s'agit ici d'une méthode en 4 étapes :
* extraction monolingue de termes monolingues simples et composés dans des brevets monolingues
* recherche de phrases parallèles dans les brevets comparables
* extraction de termes bilingues simples et composés 
* identification des termes bilingues corrects avec un classifieur SVM incluant des traits comme la partie du discours ou la probabilité de traduction


## Le protocole
#### Extraction monolingue de termes
Dans le cas de termes simples, on prend les mots tels qu'ils sont.

Dans le cas de termes composés, on extrait les phrases nominales contenant moins de 5 mots uniquement (utilisation d'expressions régulières).



#### Recherche de phrases parallèles
Pour l'extraction de paires de phrases, utilisation d'un aligneur.

On réalise ensuite un filtrage. Pour filtrer les alignements incorrects, on se base sur 3 mesures :
* score basé sur la longueur
* score basé sur un dictionnaire
* score de probabilité de traduction bidirectionnelle



#### Extraction de termes bilingues
Avec les phrases alignées, réalisation d'un alignement au mot. 




#### Identification des termes bilingues corrects
Utilisation d'un classifieur SVM. Les traits retenus sont :
* linguistiques
* statistiques




## Expérimentations

#### Données
* 7000 brevets comparables EN-ZH POS-taggés (26.8M mots EN - 25.6M mots ZH)
* Aligneur _Champollion_ pour les phrases
* Aligneur _Giza++_ pour les mots
* Dict. ZH-EN composé de _LDCCEDIC2.0_, termes bilingues de _HowNet_ et lexique bilingue contenu dans _Champollion_


#### Résultats
