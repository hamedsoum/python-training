from random import random
from unicodedata import name
import uuid


class user:
    def __init__(self,firstName,lastName, age, password):
        self.id = uuid.uuid1()
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.password = password
        pass


user1 =  user('soumahoro','hamed', 24, '12345')

print(user1.id)

print ("The random id using uuid1() is : ",end="")
print (uuid.uuid1())