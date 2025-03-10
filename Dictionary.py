profile={"FName":"Prashant","LName":"Mishra","Age":"21"}
print(profile)
print(profile["FName"])
print(profile["FName"])
print(profile.get("Age"))
print(profile.get("Aage"))
profile["Age"]="22"
print(profile)
for key in profile:
    print(key)

for key in profile:
    print(key,profile[key])

for key,val in profile.items():
    print(key,val)

if "FName" in profile:
    print("Present")

else:
    print("Absent")

print(len(profile))
print(type(profile))
profile["City"]="Lucknow"
print(profile) 
profile.pop("Age")
print(profile)
print(profile.popitem())
print(profile)
del profile["LName"]
print(profile)
profile_copy=profile.copy() 
tea_shop={"chai":{"masala":"spicy","ginger":"zesty"},
          "tea":{"mint":"cool","green":"mild","black":"strong"}
        }

print(tea_shop)

print(tea_shop["chai"])
print(tea_shop["chai"]["ginger"])

squred_num={x:x**2 for x in range(10)}
print(squred_num)
squred_num.clear()
print(squred_num)

keys=["masala","ginger","mint"]
def_val="delicious"

new_dict=dict.fromkeys(keys,def_val)
print(new_dict)

new_dict=dict.fromkeys(keys,keys)
print(new_dict)