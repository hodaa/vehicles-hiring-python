from flask_pymysql import MySQL

class VehicleRepository:

    def __init__(self):
        self.db = MySQL()

    def getById(self, vehicle_id):
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT * FROM vehicles where id= %s", vehicle_id)
        item = cursor.fetchone()
        return item if item else False



