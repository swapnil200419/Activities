"""
Earthquake Impact: Input some numbers, do some simple arithmetic
"""

m = float(input("Enter magnitude of Earthquake: "))

if m<2:
    print("Micro Earthquake")
elif 2<=m<3:
    print("Very Minor Earthquake")
elif 3<=m<4:
    print("Minor Earthquake")
elif 4<=m<5:
    print("Light Earthquake")
elif 5<=m<6:
    print("Moderate Earthquake")
elif 6<=m<7:
    print("Strong Earthquake")
elif 7<=m<8:
    print("Major Earthquake")
else:
    print("Great Earthquake")