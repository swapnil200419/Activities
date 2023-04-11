"""
Exercise basic class
Write a Python class,
MedPlus, that has three instance variables of type str, int, and float, that respectively represent the name of the medicine, batch number, and its price.
Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type
If the user passes invalid parameters to the constructor method in that case raise an appropriate error to the user of your class
"""

class Medplus:
    def __init__(self,medicine:str,batch_number:int,price:float):
        self.medicine=medicine
        self.batch_number=batch_number
        self.price=price
    def set_medicine(self,medicine:str):
        self.medicine=medicine
    def set_batch_number(self,batch_number:int):
        self.batch_number=batch_number
    def set_price(self,price:float):
        self.price=price
    def get_medicine(self)->str:
        return self.medicine
    def get_batch_number(self)->int:
        return self.batch_number
    def get_price(self)->float:
        return self.price
A=Medplus("zedplus",23,54.0)
print(A.get_medicine())
print(A.get_batch_number())
print(A.get_price())