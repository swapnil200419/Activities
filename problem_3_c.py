"""
wind
"""

T=float(input("Enter temperature in °C: "))
w=float(input("Enter wind speed in Km/h: "))
def temp_wind(T,w):
    output= 13.12 + 0.6215*T - 11.37*(w**0.16) + 0.3965*T*(w**0.16) 
    return round(output,2)
print(temp_wind(T,w),"°C")