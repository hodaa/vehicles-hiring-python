import os
from flask import request
from flask import Flask
from flask_pymysql import MySQL
from flask import jsonify
from flask import make_response
# from app.services import CustomerService
# from app.controllers import HomeController
# # from flask import Blueprint
from app.routes.customers  import customers_bp
from app.routes.vehicles  import vehicles_bp


# def create_app(config_filename):
#     app = Flask(__name__)
#     app.config.from_pyfile(config_filename)
#
#     from app.model import db
#     db.init_app(app)
#
#     from yourapplication.views.admin import admin
#     from yourapplication.views.frontend import frontend
#     app.register_blueprint(admin)
#     app.register_blueprint(frontend)
#
#     return app

#
# def create_app() -> Flask:
#
#     app = Flask(__name__)
#
#     # mysql_1 = MySQL(app,prefix='mysql1', host = os.getenv(“db_host”), user = os.getenv(“db_username”), password = os.getenv(“db_pass”), db = os.getenv(“db_name), autocommit = True, cursorclass = pymysql.cursors.DictCursor)
#     # app.config['MYSQL_HOST'] = 'db'
#     # app.config['MYSQL_USER'] = 'root'
#     # app.config['MYSQL_PASSWORD'] = 'root'
#     # app.config['MYSQL_DB'] = 'vehicles_hiring'
#
#     # app.container = container
#     # app.add_url_rule("/", "index", views.index)
#     #
#     # bootstrap = Bootstrap()
#     # bootstrap.init_app(app)
#
#     return app

#
#
#


app = Flask(__name__)
app.register_blueprint(customers_bp)
app.register_blueprint(vehicles_bp)

pymysql_connect_kwargs = {'user': os.environ.get('DB_USER', 'root'),
                          'password': os.environ.get('DB_PASSWORD', 'root'),
                          'host': os.environ.get('DB_HOST', 'db'),
                          'database': os.environ.get('DB_NAME', 'vehicles_hiring')
                          }

app.config['pymysql_kwargs'] = pymysql_connect_kwargs
mysql = MySQL(app)

@app.route('/')
def index():
    port= os.environ.get('PORT')
    return make_response(jsonify({'id':port}))

# @app.route('/api/v1/book', methods=['POST'])
# def book():
#     if request.method == 'POST' and 'email' in request.form:
#         email = request.form['email']
#         account = CustomerService.CustomerService(mysql).isExist(email)
#         print("hoda")
#         if account:
#             return make_response(jsonify({"todo": email}))
#         else:
#             CustomerService.CustomerService(mysql).addCustomer(request.form['name'], request.form['email'])
#             return make_response(jsonify({"todo": "in"}))
#
#         # service = customer_service.CustomerService(mysql)
#         # exist = service.isExist(email)
#         # print(exist)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
