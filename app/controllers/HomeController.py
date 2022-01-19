from app.repositories.CustomerRepository import CustomerRepository
from app.repositories.VehicleRepository import VehicleRepository
from app.repositories.HiringRepository import HiringRepository
from app.services.CustomerService import CustomerService
from app.services.HiringService import HiringService

from flask import request
from flask import make_response
from flask import jsonify

class HomeController:

    def index(self):
       return "I am in here"

    def hire(self,vehicle_id):

        not_valid = HiringService().validate(request.form)
        if not_valid:
           return make_response({'message': not_valid})

       #TODO check availability
        vehicle= VehicleRepository().getById(vehicle_id)
        if vehicle: # validation pass
            customer_id = CustomerRepository().getByEmail(request.form['email'])
            if customer_id is False:
                CustomerRepository().create(request.form['name'],request.form['email'])

            HiringRepository().hire(vehicle_id,customer_id,request.form)
            return make_response(jsonify(['The Vehicle is Hired for you']))
        else:
            return make_response(jsonify('message','This vehicle Id does not exist'))



