import mysql.connector
#Se instalo mysql para poder usarlo


class DAO():
    def __init__(self):
        try:
            self.conexion = mysql()
        except:
            pass

