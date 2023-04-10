from connecter_a_bdd import *
from produit import *
from tkinter import *
class Categorie(connecter_bdd):
    def __init__(self,master):
        connecter_bdd.__init__(self)
        self.master = master
        self.master.title("Gestion des produits")
        
        # create widgets for inputting data
        self.nom_label = Label(self.master, text="Nom:")
        self.nom_entry = Entry(self.master)

        self.id_label = Label(self.master, text="id:")
        self.id_entry = Entry(self.master)
        
        # create buttons for performing actions
        self.create_button = Button(self.master, text="Créer", command=self.create_recordc)
        self.update_button = Button(self.master, text="Mettre à jour", command=self.update_recordc)
        self.delete_button = Button(self.master, text="Supprimer", command=self.delete_recordc)
        
        # layout the widgets using grid
        self.nom_label.grid(row=0, column=0)
        self.nom_entry.grid(row=0, column=1)
        
        self.id_label.grid(row=5, column=0)
        self.id_entry.grid(row=5, column=1)
        
        self.create_button.grid(row=6, column=0)
        self.update_button.grid(row=6, column=1)
        self.delete_button.grid(row=6, column=2)
    def create_recordc(self):
        # get input data from widgets
        nom = self.nom_entry.get()
        # perform database operation
        try:
            categorie_id = Categorie.create(self, nom)
            messagebox.showinfo("Succès", f"Produit créé avec l'id {categorie_id}")
            self.nom_entry.delete(0, END)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de créer le produit: {str(e)}")

    def update_recordc(self):
        # get input data from widgets
     
        nom = self.nom_entry.get()
        id = self.id_entry.get()
        
        # perform database operation
        Categorie.update(self, id, nom)
        self.nom_entry.delete(0, END)
        self.id_entry.delete(0,END)
    
    def delete_recordc(self):
        id = self.id_entry.get()
        
        # perform database operation
        try:
            Categorie.delete(self, id)
            messagebox.showinfo("Succès", "Categorie supprimé avec succès")
            self.id_entry.delete(0,END)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de supprimer le produit: {str(e)}")
    def create(self, nom):
        cursor = self.bdd.cursor()
        query = "INSERT INTO categorie (nom) VALUES (%s)"
        values = (nom,)
        cursor.execute(query, values)
        self.bdd.commit()
        return cursor.lastrowid

    def update(self, id, nom):
        cursor = self.bdd.cursor()
        query = "UPDATE categorie SET nom = %s WHERE id = %s"
        values = (nom, id)
        cursor.execute(query, values)
        self.bdd.commit()

    def delete(self, id):
        cursor = self.bdd.cursor()
        query = "DELETE FROM categorie WHERE id = %s"
        values = (id,)
        cursor.execute(query, values)
        self.bdd.commit()

