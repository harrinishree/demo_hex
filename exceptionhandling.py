class salarynotinrange(Exception):
    def __init__(self, salary,message="Salary is not in (5000,20000)range"):
        self.salary = salary
        self.message = message
        #super().__init__(self.message)
        print("salary is in range")
try:
    salary=int(input("Enter the salary: "))
    if not 5000<=salary<=10000:
        raise salarynotinrange(salary)
    else:
        print("salary is in range")
except salarynotinrange as e :
    print(e)
