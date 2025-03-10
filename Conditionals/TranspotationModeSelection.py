distance=int(input("Enter the Distance:"))

if distance<3:
    mode="Walk"

elif distance<=15:
    mode="Bike"

else:
    mode="Car"

print("Mode of Transport:",mode)    