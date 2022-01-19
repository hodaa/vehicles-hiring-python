from datetime import datetime,date,timedelta
import numpy as np





class HiringService:

    def validate(self,data):
        if ('start_date' in data) is False:
            return "Please enter start date"
        if ('return_date' in data) is False:
            return "Please enter return date"
        if ('email' in data) is False:
            return "Please enter email"
        if ('name' in data) is False:
            return "Please enter name"
        if ('price' in data) is False:
            return "Please enter price"
        not_valid = self.cheek_period(data['start_date'], data['return_date'])
        if not_valid:
            return not_valid
        return self.cheek_hiring_date_in_future(data['start_date'])



    def cheek_period(self,start_date,return_date):
        start = datetime.strptime(start_date, "%d/%m/%Y")
        end = datetime.strptime(return_date, "%d/%m/%Y")
        diff = end.date() - start.date()
        print(diff.days)
        if diff.days < 0:
            return "Return date should be after start date. "
        if diff.days > 7 :
            return "A customer cannot hire a car for longer than a week. "


    def cheek_hiring_date_in_future(self,start_date):
        diff = datetime.strptime(start_date, "%d/%m/%Y") - datetime.now()
        print("diff",diff.days)
        if diff.days > 7:
            return "You can't book a vehicle up to 7 days in advance "
        if diff.days < 0:
            return "Start data should be after Yesterday "




