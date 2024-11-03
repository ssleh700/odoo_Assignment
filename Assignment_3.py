import datetime

class Employee:
    id_count = 1
    employee = []
    
    def __init__(self, emp_data):
        self.id = Employee.id_count
        Employee.id_count += 1
        self.emp_id = emp_data['emp_id']
        self.name = emp_data['name']
        self.joining_date = emp_data['joining_date']
        self.salary = emp_data['salary']
    
    @classmethod
    def create(cls, emp_data):
        emp = Employee(emp_data)
        cls.employee.append(emp)
        return emp
    
    def save(self):
        Employee.employee.append(self)
    
    @classmethod
    def update(cls, emp_id, data):
        for emp in cls.employee:
            if emp.emp_id == emp_id:
                if 'name' in data and data['name']:
                    emp.name = data['name']
                if 'joining_date' in data and data['joining_date']:
                    emp.joining_date = data['joining_date']
                if 'salary' in data and data['salary']:
                    emp.salary = data['salary']
                return print("\nDone\n")
    
    @classmethod
    def delete(cls, emp_id):
        cls.employee = [emp for emp in cls.employee if emp.emp_id != emp_id]
        print("\nDone\n")
    
    @classmethod
    def list(cls, search_term=None, sort_by=None):
        result = cls.employee
        if search_term:
            result = [emp for emp in cls.employee if emp.emp_id == search_term or emp.name == search_term]
        
        if sort_by:
            result = sorted(result, key=lambda emp: getattr(emp, sort_by))
        
        return result
    @classmethod
    def employee_exists(cls, emp_id):
        return any((emp.emp_id or emp.name) == emp_id for emp in cls.employee)
    
    def __repr__(self):
        return f"Employee(emp_id={self.emp_id}, name={self.name}, joining_date={self.joining_date}, salary={self.salary})"


while True==True:
    ch=input("enter\n 1 to create employee\n2 to update employee\n3 to delete\n4 to search\n5 to sorting\n6 to exit\n")
    if ch=='1':
        emp_id=input("enter employee ID:")
        if not Employee.employee_exists(emp_id):
            Employee.create({'emp_id':emp_id, 'name': input("enter employee name:"), 'joining_date': datetime.date.today(), 'salary': input("enter employee salary:")})
        else:
            print("\nEmployee ID is exists\n")
    elif ch=='2':
        emp_id=input("enter employee ID:")
        if  Employee.employee_exists(emp_id):
            Employee.update(emp_id, {'name': input("enter employee name"), 'salary': input("enter employee salary:")})
        else:
            print("\nEmployee not exists\n") 
    elif ch=='3':
        emp_id=input("enter employee ID:")
        if  Employee.employee_exists(emp_id):
            Employee.delete(emp_id)
        else:
            print("\nEmployee not exists\n")
    elif ch=='4':
        emp_=input("enter employee ID or name:")
        if  Employee.employee_exists(emp_):
            print(f'\n{Employee.list(search_term=emp_)}\n')
        else:
            print("\nEmployee not exists\n")
    elif ch=='5':
        print(f'\n{Employee.list(sort_by='emp_id')}\n')
    elif ch=='6':exit()
