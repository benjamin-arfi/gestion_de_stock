import mysql.connector
class connecter_bdd:
    def __init__(self):
        self.bdd = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Binyaminarfi26+",
            database="boutique"
        )