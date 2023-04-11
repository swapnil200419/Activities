"""
conversion
"""

a=float(input("Enter distance in Kilometers: "))
def centimeters(a):
    conversion=a*100000
    return conversion
print(centimeters(a),"cm")
def km_meter(a):
    conversion=a*1000
    return conversion
print(km_meter(a),"meters")
b=float(input("Enter the weight of oil in Kilograms: "))
def kg_gram(b):
    conversion=b*1000
    return conversion
print(kg_gram(b),"grams")
def kg_litre(b):
    conversion=b*1.1364
    return conversion
print(kg_litre(b),"litres")
g=float(input("Enter the time in hour: "))
def t_min(g):
    conversion=g*60
    return conversion
print(t_min(g),"minutes")
def t_sec(g):
    conversion=g*3600
    return conversion
print(t_sec(g),"seconds")