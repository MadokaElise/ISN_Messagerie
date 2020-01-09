#!usr/bin/python3.5
#-*-encoding:UTF-8-*-


#Serveur : Reçois les connexions, listes les connexions, reçois et redistribu
#les messages.

#Bibliothèques :

import socket
import select


#Variables :

port=11000
host=''
serveurOuvert = True #Permet de fermer ou d'ouvrire la boucle du programme.
msg=''
listeClients = []
lireClient = []

#Main :
print("*********Serveur*********")
print("Initilisation du serveur :")

connexionPrincipal = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connexionPrincipal.bind((host,port))
connexionPrincipal.listen(10)

print('Serveur ouvert, port :{}'.format(port))

while serveurOuvert:

    try :
        connexionDemendees,liste1,liste2 = select.select([connexionPrincipal],[],[],0.05)
    except ValueError:
        pass 

    for connexion in connexionDemendees:
        connexionClient,infos=connexion.accept()
        listeClients.append(connexionClient)
        print(listeClients)

    try:
        lireClient,liste3,liste4 = select.select(listeClients,[],[],0.05)
    except select.error:
        pass

    for client in lireClient:
        try :
            msg = client.recv(1024)
        except ConnectionResetError :
            print('Plus de client fin du serveur')
            connexionPrincipal.close()
        else :
            print(msg.decode())
            envoyeur = client
        if msg.decode() == 'end\n':
            serveurOuvert=False
        for autre in listeClients:
            try:
                if autre != envoyeur:
                    autre.send(msg)
            except BrokenPipeError:
                print("Déconnexion d'un utiisateur")
                break

connexionPrincipal.close()




