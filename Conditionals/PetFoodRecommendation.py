species=str(input("Enter your species type:"))
age=int(input("Enter your species age:"))

if species=="Dog" and age<2:
    food="Puppy food"

elif species=="Dog" and age>2:
    food="Adult food"

elif species=="Cat" and age<5:
    food="Juniour Cat food" 

elif species=="Cat" and age>5:
    food="Seniour Cat food"    

print("AI recommend:",food)
