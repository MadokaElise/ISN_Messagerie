import socket


# Création de la classe permettant d'ouvrire une connexion avec le serveur,
# d'envoyer et de recevoir des messages :

class connexion(socket.socket):  # Créer une classe dérivée d'un socket.

    def __init__(self, host, port):
        socket.socket.__init__(self)  # Initilaise l'objet.

        self.host = host  # recupère les informations utiles à la connection.
        self.port = port

        self.connexionPrincipal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Défini le type de connection.
        self.connexionPrincipal.connect((host, port))  # Etablie la connection.

        self.connexionPrincipal.setblocking(0)  # Permet de rendre les méthodes des sockets non bloquants

    def envoye_msg(self, msg):  # Fonction permettant d'envoyer un message.
        self.msg_envoye = msg.encode()  # Met en bytes les messages.
        self.connexionPrincipal.send(self.msg_envoye)  # Envoie les messages.

    def recevoir_msg(self):  # Fonction permettant de recevoir les messages (retourne un string)
        try:
            self.msg_recu = self.connexionPrincipal.recv(1024)
        except BlockingIOError:  # Si aucun message n'est recu, on passe a la suite.
            pass
        else:
            self.msg_recu = self.msg_recu.decode()  # Le message est est décodé.
            return self.msg_recu  # retourne le message recu.
