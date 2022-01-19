from app.routes import vehicles_bp
from app.controllers.HomeController import HomeController


controller = HomeController()
# customers_bp.route('<int:user_id>', methods=['GET'])(controller.index)
vehicles_bp.route('vehicles/<int:vehicle_id>/hire', methods=['POST'])(controller.hire)


