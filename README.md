Ateliers de programmation Montréal-Python
=========================================

Ce dépôt git contient les notebooks de code pour les soirées de programmation
organisées par [Montréal-Python](https://montrealpython.org/en/).
Cliquez [ici](https://www.meetup.com/Montreal-Python/events/) pour voir les prochaines dates des événements.


## Contenu

Tous les fichiers notebook se trouvent dans le sous-répertoire [`notebooks/`](./notebooks/).


### Qu'est c'est ça un notebook?

Le notebooks jupyter sont une façon de rouler du code Python de façon interactive.
Vous tapez des commandes Python dans les cases "code" et lorsque vous pesez SHIFT+ENTER
le code sera exécute et le résultat s'affichera en dessous:

```Python
 In[1]: x = 3
 In[2]: x*2
Out[2]: 6
```

Vous pouvez télécharger les fichiers notebooks (extension `.ipynb`) sur votre ordinateur
et les rouler localement ou encore mieux rouler les notebooks en ligne sans avoir
à installer. Plus d'infos suivent.


## Rouler un notebook en ligne

Vous n'avez pas besoin de rien installer pour essayer les notebooks qui se trouvent
dans ce dépôt. Visitez la page [`notebooks/README.md`](./notebooks/README.md)
pour voir la liste de tous les notebooks. Pour chaque notebook, nous avons 
préparé des liens "launch binder" et "Open in Colab". 

### Utiliser les liens "launch binder"

Cliquez sur le bouton pour lancer une instance JupyterLab temporaire dans le nuage:  
![launch binder button](./assets/launch-binder-button.png)

[Binder](https://mybinder.org/) est un service qui permet de rouler une instance
temporaire JupyterLab sur un ordinateur offert par des organisations comme
Google Cloud, OVH, GESIS Notebooks et Turing Institute.

TODO:
- explain instance will shutdown after a period of inactivity
  Binder will automatically shut down user sessions that have more than 10 minutes of inactivity
- you can download the notebook using the button...
  IMG



### Utiliser les liens "Open in Colab"

Cliquez sur le bouton pour ouvrir le fichier dans Google Colab:  
![launch binder button](./assets/Open-in-Colab-button.png)

TODO:
- you will need to Authorize Run
  IMG
- need to add Colab app to your google drive 
  IMG



## Rouler un notebook localement

Si vous avez un fichier notebook (extension `.ipynb`) sur votre ordi


### Utiliser JupyterLab Desktop

Install 
https://github.com/jupyterlab/jupyterlab-desktop#jupyterlab-desktop
(choisir des liens Download plus bas sur la page)


### Utiliser Google Colab

Ajouter le fichier notebook à votre google drive

- need to add Colab app to your google drive 
  IMG



### Installer JupyterLab avec pip

Cette option est pour les utilisateurs avancées qui connaissent le terminal des commandes.

- Download Python
- Install
- Open command line
- Create virtualenv venv
  - Run python -m pip install jupyterlab
  - Run python -m pip install pandas requests beautifulsoup4 feedparser
  - Start JupyterLab by running `jupyter-lab`





## Créer un nouveau notebook

Dans JupterLab

Dans Google Colab, visitez https://colab.research.google.com/ et choisissez
l'option "New Notebook"



