from connecter_a_bdd import *
from tkinter import *

class affiche_produit(connecter_bdd):
    def __init__(self, master):
        self.master = master
        connecter_bdd.__init__(self)
        self.master.title("Afficher les produits")
        # Créer une Listbox pour afficher les données
        self.listbox = Listbox(self.master, width=120, height=20)
        self.afficher_produits()
        self.listbox.pack()

    def afficher_produits(self):
        cursor = self.bdd.cursor(dictionary=True)
        query = "SELECT * FROM produit"
        cursor.execute(query)
        result = cursor.fetchall()
        
        # Ajouter les données à la Listbox
        for row in result:
            self.listbox.insert(END, row)



