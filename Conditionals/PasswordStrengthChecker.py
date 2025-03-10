password=input("Enter your Password:")
char=len(password)

if char<6:
    strength="Weak"

elif char<=10:
    strength="Medium"

else:
   strength="Strong"

print("Password strength:",strength)   