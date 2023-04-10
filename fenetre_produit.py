from connecter_a_bdd import *
from tkinter import *

class AfficheProduit(connecter_bdd):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Afficher les produits")
        
        # Créer une Listbox pour afficher les données
        self.listbox = Listbox(self.master, width=120, height=20)
        self.listbox.pack()
        
        # Bouton pour filtrer les produits par catégorie
        self.categorie_entry = Entry(self.master)
        self.categorie_entry.pack()
        self.filtrer_button = Button(self.master, text="Filtrer", command=self.filtre)
        self.filtrer_button.pack()
        
        # Afficher tous les produits
        self.afficher_produits()
    def filtre (self):

        id_categorie = self.categorie_entry.get()

        AfficheProduit.filtrer_produits(self, id_categorie)
        self.categorie_entry.delete(0, END)

    def filtrer_produits(self,id_categorie):
        cursor = self.bdd.cursor(dictionary=True)
        query = "SELECT * FROM produit WHERE id_categorie = %s"
        values = (id_categorie,)
        cursor.execute(query,values)
        result = cursor.fetchall()
        self.listbox.delete(0, END)
        for row in result:
            self.listbox.insert(END, row)

    def afficher_produits(self):
        cursor = self.bdd.cursor(dictionary=True)
        query = "SELECT * FROM produit"
        cursor.execute(query)
        result = cursor.fetchall()
        self.listbox.delete(0, END)
        for row in result:
            self.listbox.insert(END, row)



