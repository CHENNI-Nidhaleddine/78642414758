<!-- GETTING STARTED -->
## Description:
Dans le cadre du premier TP du projet de spécialité, nous avons implémenté différents algorithmes de détection de communautés, notamment la version améliorée de Louvain qui initialise les communautés par des cliques, suivi de Semi-synchronous-LPA avec ses 3 variantes : LPA-prec, LPA-max, LPA-prec-max. 
Pour la démonstration de nos algorithmes, nous avons utilisé Streamlit, une bibliothèque Python qui permet de créer des applications web interactives à l'aide de scripts Python. L’exécution de ce code va permettre d'interagir avec l’application mise en oeuvre en local.

### Dossiers:
#### /pages: 
contient l'implémentation des 3 algorithmes
#### /data:
contient les datasets réels 
#### /Sources:
contient le code c++ pour la génération du benchmark des dataset synthétiques 
<!-- GETTING STARTED -->
## Getting Started
Pour avoir une copie en local

### Prerequis

Python

### Installation

1. Cloner le repo
   ```sh
    $ git clone https://github.com/CHENNI-Nidhaleddine/TP1_NUTONOMY
   ```
2. Installer les Requirements 
   ```sh
    $ pip install -r requirements.txt 
   ```

## Execution 
   ```sh
    $ streamlit run Main.py 
   ```
