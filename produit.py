from connecter_a_bdd import *
from tkinter import*
from tkinter import messagebox
class ProduitGUI(connecter_bdd):
    def __init__(self, master):
        connecter_bdd.__init__(self)
        self.master = master
        self.master.title("Gestion des produits")
        
        # create widgets for inputting data
        self.nom_label = Label(self.master, text="Nom:")
        self.nom_entry = Entry(self.master)
        
        self.desc_label = Label(self.master, text="Description:")
        self.desc_entry = Entry(self.master)
        
        self.prix_label = Label(self.master, text="Prix:")
        self.prix_entry = Entry(self.master)
        
        self.quant_label = Label(self.master, text="Quantité:")
        self.quant_entry = Entry(self.master)
        
        self.categ_label = Label(self.master, text="categorie:")
        self.categ_entry = Entry(self.master)

        self.id_label = Label(self.master, text="id:")
        self.id_entry = Entry(self.master)
        
        # create buttons for performing actions
        self.create_button = Button(self.master, text="Créer", command=self.create_record)
        self.update_button = Button(self.master, text="Mettre à jour", command=self.update_record)
        self.delete_button = Button(self.master, text="Supprimer", command=self.delete_record)
        
        # layout the widgets using grid
        self.nom_label.grid(row=0, column=0)
        self.nom_entry.grid(row=0, column=1)
        
        self.desc_label.grid(row=1, column=0)
        self.desc_entry.grid(row=1, column=1)
        
        self.prix_label.grid(row=2, column=0)
        self.prix_entry.grid(row=2, column=1)
        
        self.quant_label.grid(row=3, column=0)
        self.quant_entry.grid(row=3, column=1)
        
        self.categ_label.grid(row=4, column=0)
        self.categ_entry.grid(row=4, column=1)

        self.id_label.grid(row=5, column=0)
        self.id_entry.grid(row=5, column=1)
        
        self.create_button.grid(row=6, column=0)
        self.update_button.grid(row=6, column=1)
        self.delete_button.grid(row=6, column=2)
        
        self.nom_entry.delete(0, END)
        self.desc_entry.delete(0, END)
        self.prix_entry.delete(0, END)
        self.quant_entry.delete(0, END)
        self.categ_entry.delete(0, END)
    def create_record(self):
        # get input data from widgets
        nom = self.nom_entry.get()
        description = self.desc_entry.get()
        prix = self.prix_entry.get()
        quantite = self.quant_entry.get()
        id_categorie = self.categ_entry.get()
        
        # perform database operation
        try:
            produit_id = ProduitGUI.create(self, nom, description, prix, quantite, id_categorie)
            messagebox.showinfo("Succès", f"Produit créé avec l'id {produit_id}")
            self.nom_entry.delete(0, END)
            self.desc_entry.delete(0, END)
            self.prix_entry.delete(0, END)
            self.quant_entry.delete(0, END)
            self.categ_entry.delete(0, END)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de créer le produit: {str(e)}")
    
    def update_record(self):
        # get input data from widgets
     
        nom = self.nom_entry.get()
        description = self.desc_entry.get()
        prix = self.prix_entry.get()
        quantite = self.quant_entry.get()
        id_categorie = self.categ_entry.get()
        id = self.id_entry.get()
        
        # perform database operation
        ProduitGUI.update(self, nom, description, prix, quantite, id_categorie, id)
        self.nom_entry.delete(0, END)
        self.desc_entry.delete(0, END)
        self.prix_entry.delete(0, END)
        self.quant_entry.delete(0, END)
        self.categ_entry.delete(0, END)
        self.id_entry.delete(0,END)
    
    def delete_record(self):
        id = self.id_entry.get()
        
        # perform database operation
        try:
            ProduitGUI.delete(self, id)
            messagebox.showinfo("Succès", "Produit supprimé avec succès")
            self.id_entry.delete(0,END)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de supprimer le produit: {str(e)}")
    
    

    def create(self, nom, description, prix, quantite,id_categorie):
        cursor = self.bdd.cursor()
        query = "INSERT INTO produit (nom, description, prix, quantite,id_categorie) VALUES (%s, %s, %s, %s,%s)"
        values = (nom, description, prix, quantite,id_categorie)
        cursor.execute(query, values)
        self.bdd.commit()
        return cursor.lastrowid

    def update(self, nom, description, prix, quantite,id_categorie,id):
        cursor = self.bdd.cursor()
        query = "UPDATE produit SET nom = %s, description = %s, prix = %s, quantite = %s, id_categorie = %s WHERE id = %s"
        values = (nom, description, prix, quantite,id_categorie,id)
        cursor.execute(query, values)
        self.bdd.commit()

    def delete(self, id):
        cursor = self.bdd.cursor()
        query = "DELETE FROM produit WHERE id = %s"
        values = (id,)
        cursor.execute(query, values)
        self.bdd.commit()
