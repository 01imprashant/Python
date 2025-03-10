order_size=str(input("Enter the size of coffee:"))
extra_shot=True

if extra_shot:
    coffee=order_size + " coffee with an Extra shot"

else:
    coffee=order_size + " coffee"

print("Order:",coffee)        