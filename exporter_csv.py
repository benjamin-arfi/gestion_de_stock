import csv
from connecter_a_bdd import *
from tkinter import*

class ExportCSV(connecter_bdd):
    def __init__(self,master):
        connecter_bdd.__init__(self)
        self.master = master
        self.exporter()
        

    def exporter(self):
        cursor = self.bdd.cursor(dictionary=True)
        query = f"SELECT * FROM produit"
        cursor.execute(query)
        result = cursor.fetchall()
        with open("produits.csv", 'w', newline='',encoding='utf-8') as csvfile:
            fieldnames = [desc[0] for desc in cursor.description]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
            writer.writeheader()
            for row in result:
                writer.writerow(row)

