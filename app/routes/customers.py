from app.routes import customers_bp
from app.controllers.HomeController import HomeController
from flask_pymysql import MySQL

controller = HomeController()
# customers_bp.route('<int:user_id>', methods=['GET'])(controller.index)
customers_bp.route('customers', methods=['GET'])(controller.index)


