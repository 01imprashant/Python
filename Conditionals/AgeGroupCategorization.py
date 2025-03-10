age=int(input("Enter your age:"))

if age<13:
    category="Child"

elif age<20:
    category="Teenager"

elif age<60:
    category="Adult"

else:
    category="Seniour"

print("Category:",category)    
