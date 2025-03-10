tea_type=("masala","ginger","green")
print(tea_type)
print(tea_type[0]) 
print(tea_type[-1])
print(tea_type[:])  
print(tea_type[0:])
print(tea_type[:2]) 
# tea_type[0]="lemon" 
print(len(tea_type))
more_tea=("herbal","kulladh","ai")
print(more_tea)
all_tea=more_tea+tea_type
print(all_tea)  
if "green" in all_tea:
    print("presnt") 

more_tea=("herbal","green","mint","mint")
print(more_tea)
print(more_tea.count("mint"))
print(more_tea.count("minti"))
print(tea_type)
(Masala,Ginger,Green)=tea_type
print(Masala)
print(type(tea_type))
new_tea=("chai",(1,2,3,4),"chaiya")
print(new_tea)
