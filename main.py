from tkinter import *
from categorie import *
from produit import *
from fenetre_categorie import *
from fenetre_produit import*

class App:
    def __init__(self, master):
        self.master = master
        master.title("Tableau de bord")

        self.create_button_categorie = Button(master, text="Créer categorie", command=self.open_categorie)
        self.create_button_categorie.grid(row=1, column=1)

        self.create_button_produit = Button(master, text="Créer produit", command=self.open_produit)
        self.create_button_produit.grid(row=2, column=1)

        self.open_button_produit = Button(master, text="ouvrir la liste des produits", command=self.liste_produit)
        self.open_button_produit.grid(row=3, column=1)

        self.open_button_categorie = Button(master, text="ouvrir la liste des categories", command=self.liste_categorie)
        self.open_button_categorie.grid(row=4, column=1)

    def open_categorie(self):
        self.master.withdraw()  # cacher la fenêtre principale
        create_window = Toplevel(self.master)
        create_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close(create_window))
        Categorie(create_window)

    def open_produit(self):
        self.master.withdraw()  # cacher la fenêtre principale
        update_window = Toplevel(self.master)
        update_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close(update_window))
        ProduitGUI(update_window)

    def liste_produit(self):
        self.master.withdraw()  # cacher la fenêtre principale
        liste_window = Toplevel(self.master)
        liste_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close(liste_window))
        affiche_produit(liste_window)

    def liste_categorie(self):
        self.master.withdraw()  # cacher la fenêtre principale
        liste_categorie_window = Toplevel(self.master)
        liste_categorie_window.protocol("WM_DELETE_WINDOW", lambda: self.on_close(liste_categorie_window))
        affiche_categorie(liste_categorie_window)

    def on_close(self, window):
        window.destroy()  # détruire la fenêtre actuelle
        self.master.deiconify()  # restaurer la fenêtre principale


root = Tk()
app = App(root)
root.mainloop()



       