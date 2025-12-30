# pythonpourlads

# **Présentation**
Ce projet a été réalisé par Munis El Karkari, Guilherme Bernardo et Chiara Frassu dans le cadre du cours Python pour la Data Science de Lino Galiana et Romain Avouac. Il vise à étudier le lien entre l'accès à l'information et la créativité des enfants grâce aux données de l'enquête PISA 2022. 
Nous tenterons de répondre à la problématique suivant : Existe-t-il un point optimal entre le manque d’accès à l’information et l’accès complet à celle-ci qui maximise la créativité de l’enfant ?

# **Méthodologie**
## **1. Récupération et traitement des données**

Nos données sont issues des questionnaires de l'enquête PISA 2022 menée par l'OCDE. Les données étaient disponibles au format SAV, du fait de restrictions sur la diffusion de celles-ci (confidentialité), nous avons les avons placées dans un Bucket sécurisé utilisé pour la suite de notre travail. Il s'agit de deux fichiers : le questionnaire des élèves (student_questionnaire) et les résultats aux tests de créativité (creative_thinking). Il a été nécessaire de traiter les données qui présentaient un grand nombre de valeurs manquantes afin d'éviter des biais dans notre analyse et convertir leur type afin qu'elles puissent être exploitées. 

## **2. Analyse descriptive et visualisation**

Dans cette partie, nous avons mené une analyse descriptive grâce à des statistiques descriptives et des graphiques de visualisation afin d'améliorer notre compréhension des données. Elle nous permet également de dégager des tendances préliminaires, suggérant un lien potentiel entre la disponibilité de l’information et la pratique d’activités créatives.
Nous avons dû par la suite intégrer l'utilisation des poids d’échantillonnage. Nous comparons donc les distributions en tenant compte des poids et sans en tenir compte.

## **3. Modélisation : régression linéaire**

Pour aller au-delà des tendances préliminaires identifiées par l'analyse descriptive, nous avons effectué trois régressions linéaires afin de quantifier l'effet des différents facteurs environnementaux sur la pensée créatives des élèves.
Dans un premier temps nous avons régressé la pratique d'activités créatives en dehors de l'école sur les différents facteurs potentiellement influents sans tenir compte des poids d’échantillonnage (représentativité). Dans la régression suivante, nous tenons compte de ces poids. 
Par la suite, nous avons modifié notre variable d'intérêt pour nous intéresser au score de créativité des élèves en tenant compte des poids. 

- **Variables dépendantes** : fréquence de participation à des activités créatives hors école (`creative_out`) puis score de créativité  
- **Variables explicatives** : niveau d'accès aux ressources numériques, environnement socio-économique, caractéristiques familiales, environnement scolaire, et autres facteurs contextuels disponibles dans le dataset.  

## **4. Conclusion**

Les résultats confirment partiellement l'existence d'un point optimal. Un résultat inattendu concernant l'effet des ressources numériques a émergé.

# **Structure du projet et fonctionnement**
Tout le code d'analyse, visualisation et modélisation est contenu dans le fichier `main.ipynb`.  
Le dataset provient d'un **bucket** et est importé directement dans le notebook. Le chemin d'accès aux données est défini dans le code.

Un fichier séparé contient les fonctions nécessaires à l’estimation des régressions linéaires : `functions.ipynb`. Ces fonctions ont été spécifiquement conçues pour prendre en compte les **poids d’échantillonnage PISA**, indispensables dans le cadre d’une enquête afin d’obtenir des estimations représentatives de la population étudiée.
Ces fonctions sont appelées dans le notebook principal lors de la phase de modélisation.

Pour executer le projet il suffit d'ouvrir le notebook `main.ipynb` dans VS Code, et toutes les cellules peuvent être exécutées dans l'ordre pour reproduire l'analyse.  


