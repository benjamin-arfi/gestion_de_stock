from connecter_a_bdd import *
from tkinter import *
class affiche_categorie(connecter_bdd):

    def __init__(self, master):
        self.master = master
        connecter_bdd.__init__(self)
        self.master.title("Afficher les categories")
        # Créer une Listbox pour afficher les données
        self.listbox = Listbox(self.master, width=30, height=10)
        self.afficher_categorie()
        self.listbox.pack()

    def afficher_categorie(self):
        cursor = self.bdd.cursor(dictionary=True)
        query = "SELECT * FROM categorie"
        cursor.execute(query)
        result = cursor.fetchall()
        
        # Ajouter les données à la Listbox
        for row in result:
            self.listbox.insert(END, row)