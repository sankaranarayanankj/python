class Titan:
    def __init__(self):
        self.emp_name=(input("Name:"))
        self.emp_age=int(input("Age:"))
        self.emp_city=(input("City:"))
        self.emp_phone=int(input("Phone:"))
l=[]
n=int(input("<<<---NO.of records-->>>"))
for i in range(n):
    e=Titan()
    l.append(e)
print("<<<---Get the total name and age--->>>")
print("Name\tAge")
for i in l:
    print(i.emp_name,"\t",i.emp_age)
print("<<------------------>>")
print("<<<---GET the city--->>>")
for i in l:
    print(i.emp_city)
print("<<------------------>>") 
print("<<<---Find the person--->>>")
c=0
x=input("Enter required person")
for i in l:
    if(i.emp_name==x):
        print(i.emp_phone)
        c=1
if(c==0):
    print("Employee not found")
print("<<------------------>>")
print("Class name--->>>",__name__)
print("<<------------------>>")
print("<<<--- --- ---Total Details--- --- --->>>")
for i in l:
    print(i.emp_name,'\t',i.emp_age,'\t',i.emp_city,'\t',i.emp_phone)


