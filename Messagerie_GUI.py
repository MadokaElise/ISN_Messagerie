from datetime import datetime
from tkinter import *

class VueMessages(Frame):

        def __init__(self,master=NONE):
            super().__init__(master)
            self.pack()
            #Creation zone pseudo
            self.init_zone_pseudo()
            #Creation zone texte pour les  messages
            self.init_zone_texte()
            #Creation zone message a envoyer
            self.init_zone_message()
            #Boutton quitter
            quit_bouton = Button(master, text="Quitter", command=master.quit, bg="red")
            quit_bouton.pack(side="bottom")

        def init_zone_texte(self):
            frame_zone_text = LabelFrame(self, text="Messages", padx=5, pady=50)
            self.zone_texte = Text(frame_zone_text, height=20, width=50)
            self.zone_texte.pack(padx=5, pady=5)
            self.zone_texte.pack(side="left")
            scroll_bar_text = Scrollbar(frame_zone_text)
            scroll_bar_text.pack(side="right")
            scroll_bar_text.config(command=self.zone_texte.yview)
            self.zone_texte.config(yscrollcommand=scroll_bar_text.set)
            frame_zone_text.pack()

        def init_zone_message(self):
            frame_zone_message = Label(self, padx=5, pady=5)
            message_label = Label(frame_zone_message, text="Message :", bg="grey")
            message_label.pack(side="left")
            self.message = Entry(frame_zone_message, width=50, bg="ivory")
            self.message.pack(side="left")
            frame_zone_message.pack()
            envoyer_bouton = Button(frame_zone_message,text="Envoyer",command=self.envoyer_message)
            envoyer_bouton.pack(side="right")

        def init_zone_pseudo(self):
            frame_zone_pseudo = Label(self, padx=5, pady=5)
            pseudo_label = Label(frame_zone_pseudo, text="Pseudo :", bg="grey")
            pseudo_label.pack(side="left")
            self.pseudo = Entry(frame_zone_pseudo, width=50, bg="ivory")
            self.pseudo.pack(side="left")
            frame_zone_pseudo.pack()

        def envoyer_message(self):
            msg_text = self.message.get()
            #Traitement du message : Ajout retour a la ligne
            msg_text += "\n"
            # Traitement du message : Ajout entete ( Pseudo+heure )
            msg_text =  "("+datetime.today().strftime("%H:%M:%S")+")"+self.pseudo.get()+" : "+msg_text
            #Trace dans la console
            print("Envoyer : "+msg_text)
            # Affiche notre message dans la zone de convsersation
            self.ajouter_message(msg_text)
            #reset de la zone de message
            #Envoye du message

        def ajouter_message(self,message_text):
            self.zone_texte.insert('end',message_text)

if __name__ == '__main__':
    root = Tk()
    app = VueMessages(master=root)
    app.mainloop()
