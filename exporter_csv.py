import csv
from connecter_a_bdd import *

class ExportCSV(connecter_bdd):
    def __init__(self):
        connecter_bdd.__init__(self)
    
    def exporter(self, table_name, file_name):
        cursor = self.bdd.cursor(dictionary=True)
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        result = cursor.fetchall()
        with open(file_name, 'w', newline='',encoding='utf-8') as csvfile:
            fieldnames = [desc[0] for desc in cursor.description]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
            writer.writeheader()
            for row in result:
                writer.writerow(row)



export_csv = ExportCSV()
export_csv.exporter('produit', 'produits.csv')