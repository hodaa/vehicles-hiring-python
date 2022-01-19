from flask import Blueprint
customers_bp = Blueprint('customers', __name__, url_prefix='/api/v1')
vehicles_bp = Blueprint('vehicles', __name__, url_prefix='/api/v1')
