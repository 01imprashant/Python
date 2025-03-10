chai_variety=["masala","lemon","ginger","mint"]
print(chai_variety)
print(chai_variety[0])
print(chai_variety[1])
print(chai_variety[-1])
print(chai_variety[-2])
chai_type=chai_variety[:]
print(chai_type)
chai_variety[0]="green"
print(chai_variety)
print(chai_variety[1:2])
chai_variety[1:3]=["black","white"]
print(chai_variety)
print(chai_variety[1:1])
chai_variety[1:1]=["chai","chai"]
print(chai_variety)
print(chai_variety[1:2])
print(chai_variety[1:3])
chai_variety[1:3]=[]
print(chai_variety)

for chai in chai_variety:
    print(chai,end=',')

if "black" in chai_variety:
    print("Found")

else:
    print("Not Found")    

chai_variety.append("black")
print(chai_variety)

print(chai_variety.pop())
print(chai_variety)
chai_variety.remove("lemon")
print(chai_variety)

chai_variety.insert(1,"kullad")
print(chai_variety)

chai_variety_copy=chai_variety.copy()
print(chai_variety_copy)
chai_variety_copy.append("lemon")
print(chai_variety_copy)
print(chai_variety)

range(10)
print(range)
y=range(10)
print(y)

square_num=[x**2 for x in range(10)]
print(square_num)
cube_num=[y**3 for y in range(5)]
print(cube_num)
  