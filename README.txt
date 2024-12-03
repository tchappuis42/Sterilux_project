## Description
Ce projet comprend un client développé en JavaScript et un serveur en Python. Il permet de capturer la position des clics de souris sur le client et de les transmettre au serveur en utilisant des WebSockets

## Prérequis
- pyhton 3
- python3-pip
- python WebSockets

## Lancer le projet

1. **Lancer le serveur** :  
   - Ouvrez un terminal et accédez au dossier `server` :  
     cd chemin/vers/le/dossier/server
   - Exécutez la commande suivante pour démarrer le serveur :  
     python3 server.py

2. **Lancer le client** :  
   - Dans un autre terminal, accédez au dossier `client` :  
     cd chemin/vers/le/dossier/client
   - Lancez un serveur HTTP local avec la commande suivante :  
     python3 -m http.server 8000
   - Ouvrez ensuite votre navigateur et accédez à :  
     http://localhost:8000
