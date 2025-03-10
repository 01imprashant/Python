# x=('lemon','ginger','masala','mint')
# y=enumerate(x)
# print(y)
# l=list(y)
# print(l)

# Method1
file=open('Youtube.py','w')

print(iter(file) is file)

try:
    file.write("Introduction to Python")
finally:
    file.close()    

# Method2
with open('Youtube.py','w') as file:
    file.write("Introduction to python")