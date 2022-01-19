from flask_pymysql import MySQL

class CustomerRepository:

    def __init__(self):
        self.db = MySQL()

    def getByEmail(self, email):
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT id FROM customers where email= %s", email)
        account = cursor.fetchone()
        return account[0] if account else False



    def create(self, name, email):
        sql = "INSERT INTO customers(name, email)VALUES( % s, % s)"
        data = (name, email)
        cursor = self.db.connection.cursor()
        cursor.execute(sql, data)
        self.db.connection.commit()
        cursor.close()
        # return redirect('User added successfully!')


