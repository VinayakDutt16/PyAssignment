#!/usr/bin/env python
# coding: utf-8

# In[12]:


#class is a template or blueprint for an object
class Student_Register:
    sid=10
    sName="Vinayak"
    
    def Register(self):
        print("Hello student do you want to register")


# In[2]:


#in other languages class object = new class()
#in python obj = class()
#an object is an real-time entity having characterstic and functionality
s1=Student_Register()
print(s1)


# In[4]:


print(s1.sid)
print(s1.sName)


# In[13]:


s2= Student_Register()
print(s2.sid,s2.sName)
s2.Register()


# In[20]:


#give objects memory
#constructor - method => which will initialize the memory for the object
class StudentRegister:
    def __init__(self,num):
        print("hey user",self,num)
s1=StudentRegister(101)

print(s1)
#self is an keyword which is storing the memory address of current object


# In[22]:


class StudentRegister:
    def __init__(self,num):
        self.sid=num           #varible sid made with self that is the memory address of current object
        print("hey user",self.sid)
s1=StudentRegister(101)
sd1=StudentRegister(110)


# In[34]:


class Employee:
    def __init__(self,Eid,Ename,Eaddress):#constructor of class employee
        self.eid=Eid
        self.ename=Ename
        self.eaddress=Eaddress    
    def empinfo(self):
        print("Employee Details :\nEmployee ID :",self.eid,"\nEmployee Name :",self.ename,"\nEmployee Address :",self.eaddress)
        
e1=Employee(101,"Vinayak","Sector 9,Hiranmagri")

e2=Employee(102,"Vishal","Sector 11,Gandhinagar")

e1.empinfo()

e2.empinfo()
        


# In[35]:


#uber application , driver , customer
#d_id,name,email
#customer_id, name , email , wallet

#inheritence
#father (parent class/Super class)
#child (child class/sub class/derived class)
#oops => solves real time problems=>like code duplicacy=>solved by using Inheritence


# In[37]:


class driver:
    def __init__(self,id,name,mail):
        self.id=id
        self.name=name
        self.mail=mail
    def dinfo(self):
        print("Info of the driver :",self.id,self.name,self.mail)
d1=driver(101,"Rohan","rohan99@gmail.com")
d1.dinfo()


# In[41]:


class driver:
    amount=100
    def data(self):
        print("This is an driver class")
class emp(driver):   #inheritance of driver class in the emp class driver class=> super class  / emp class => sub class
    salary=1000
e1 = emp()
e1.salary
e1.amount
e1.data()


# In[48]:


class driver:
    def __init__(self,id,name,mail):
        self.id=id
        self.name=name
        self.mail=mail
    def dinfo(self):
        print("Info of the driver :",self.id,self.name,self.mail)
        
class Employee(driver):
    def __init__(self,eid,ename,e_email):
        super().__init__(eid,ename,e_email) #super calling the function of super class
class Employee2(driver):
    def __init__(self,eid,ename,e_email,wallet):
        super().__init__(eid,ename,e_email)
        self.wallet=wallet
e1=Employee(99,"Rahul","rahul")
e2=Employee2(99,"Rahul","rahul",900)
#e1.eid not able to use because eid is assigned to super class variable id
e1.id
e2.wallet


# In[21]:


class customer:
    def __init__(self,c_id,c_name,c_salary):
        self.cid=c_id
        self.cname=c_name
        self.csal=c_salary
    def cinfo(self):
         print("Emp id :",self.cid,self.cname,self.csal)
class customerHobby(customer):
    def __init__(self,cid,cname,csal,c_hobby):
        super().__init__(cid,cname,csal)
        self.c_hobby=c_hobby
    def cinfo1(self):
        print("Emp id :",self.cid,self.cname,self.csal,self.c_hobby)
   
        
c1 = customer(101,"Vinayak",100000)
c2 = customerHobby(102,"sachin",10000,"Cricket")

c1.cinfo()

c2.cinfo1()
        


# In[ ]:




