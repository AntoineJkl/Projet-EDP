# Projet-EDP
Ce projet porte sur la réalisation d'un schéma éléments finis pour le système d'équations d'Oseen

# Description des dossiers

## ./python
Scripts python de création de mesh à partir de l'API gmsh pour python :

https://gitlab.onelab.info/gmsh/gmsh/blob/gmsh_4_8_3/api/gmsh.py

- **circle_mesh :** script de génération de mesh selon l'exemple donné dans le sujet. Il permet d'ajuster la précision *h* pour les points sur le contour et sur le cylindre ainsi que la position et la taille de ces différents éléments (conversion automatique en mesh 2D pour *FreeFem++*).
  
- **svg_profile_mesh :** script de génération de mesh à partir d'un fichier .svg en chemin correspondant au profil désiré (conversion automatique en mesh 2D pour *FreeFem++*).
  
- **convert_mesh :** script comportant une fonction *convert2D* permettant la conversion d'un mesh (par défaut 3D) généré par *gmsh* en un mesh 2D afin d'appliquer des calculs éléments finis avec *FreeFem++*.

## ./profils
Dossier comportant différents profils .svg.

## ./mesh
Dossier comportant :

- les mesh de l'exemple cylindrique pour différents paramètres

- les .mesh associés aux profils .svg et générés à partir du script *./python/svg_profile_mesh*.

On renseigne ici les caractéristiques associées à chaque mesh généré :

| Fichier             | h  | Lc | Description |
|---------------------|---:|---:|-------------|
| cylinder1.mesh    | 0.5  |  1  | *Cylindre avec un grand pas h* |
| cylinder2.mesh    | 0.2  |  1  | *Cylindre avec un pas h moyen* |
| cylinder3.mesh    | 0.1 |  1  | *Cylindre avec un petit pas h* |
| triangle1.mesh    | 0.2  |  1.225  | *Triangle pointant vers la droite* |
| triangle2.mesh    | 0.2  |  1.225  | *Triangle pointant vers la gauche* |
| square.mesh       | 0.2  |  1      | *Carré*      |
| diamond.mesh      | 0.2  |  1.414  | *Losange*    |
| pentagon.mesh     | 0.2  |  1.088  | *Pentagone*  |
| rabbit.mesh       | 0.2  |  2      | *Lapin*  |
| sum.mesh          | 0.2  |  0.850  | *Lettre sigma majuscule*  |
| crescent.mesh     | 0.2  |  2  | *Croissant de Lune*  |
|wing_propeller.mesh| 0.2  |  0.384  | *Hélice d'avion*  |
| wing_ULM.mesh     | 0.2  |  0.323  | *Aile d'ULM*  |
|wing_blackbird.mesh| 0.2  |  0.548  | *Aile de Blackbird*  |