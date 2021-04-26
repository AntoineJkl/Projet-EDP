# Description du dossier

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