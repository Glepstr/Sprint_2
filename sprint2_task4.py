class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours == 0:
            hours = (7 - rest_days) * 8
            return cls(name, hours, rest_days, email)
        else:
            return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email == '':
            email = f"{name}@email.com"
            return cls(name, hours, rest_days, email)
        else:
            return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, value):
        cls.hourly_payment = value

    def salary(self):
        sal = self.hours * self.hourly_payment
        return sal
    
EmployeeSalary.set_hourly_payment(220)
print(EmployeeSalary.hourly_payment)

jhon = EmployeeSalary("Jhon", 10, rest_days=10, email="s.s@s.s")
print(jhon.salary())