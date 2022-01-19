from flask_pymysql import MySQL

class HiringRepository:


    def __init__(self):
        self.db = MySQL()

    def hire(self,vehicle_id,customer_id,data):
        cursor = self.db.connection.cursor()
        sql = "INSERT INTO invoices(customer_id,vehicle_id,start_date,end_date,price)VALUES( % s, % s  , % s, % s, % s)"
        data = (customer_id, vehicle_id,data['start_date'],data['return_date'],data['price'])
        cursor.execute(sql,data)
        self.db.connection.commit()
        cursor.close()
        return  True



