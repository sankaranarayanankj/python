class Employee:
    def __init__(self):
        self.emp_id=int(input("ID:"))
        self.emp_name=(input("Name:"))
        self.emp_des=(input("Desigination:"))
        self.emp_sal=int(input("Salary:"))
    def category(self):
        if(self.emp_sal>=25000):
            self.cat=" Class A"
        elif(self.emp_sal>=20000 and self.emp_sal<=25000):
            self.cat=" Class B"
        elif(self.emp_sal>=15000 and self.emp_sal<=20000):
            self.cat="Class C"
        else:
            self.cat="Class D"
        obj.display_details()
    def display_details(self):
        print(self.emp_id,"<-->",self.emp_name,"<-->",self.emp_des,"<-->",self.emp_sal,"<-->",self.cat)
l=[]
x=int(input("Enter number of employees:"))
for i in range(x):
    obj=Employee()
    l.append(obj)
    print("Dict---->",Employee.__dict__)
