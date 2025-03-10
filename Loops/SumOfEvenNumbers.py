n=int(input("Enter your number:"))
sum=0

for i in range(n+1):
    if i%2==0:
        sum=i+sum
        
print("Sum of even Numbers:",sum)        