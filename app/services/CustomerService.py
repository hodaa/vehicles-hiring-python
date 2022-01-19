import app.repositories.CustomerRepository
import app.repositories.CustomerRepository


class CustomerService:

    def __init__(self, mysql):
        self.mysql = mysql

    def isExist(self, email):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT * FROM customers where email= %s", email)
        account = cursor.fetchone()
        if account:
            return True
        return False



    def book(self, request):
        exist = CustomerRepository.getByEmail(request.form['email'])


