import math

def area_and_circumference(radius):
    area=math.pi*radius**2
    circumference=2*math.pi*radius
    return area,circumference
    
radius=float(input("Enter your radius:"))

area,circumference=area_and_circumference(radius)
print("Area:",area,"Circumference:",circumference)