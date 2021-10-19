def whereIsMyFood(fridge, item):
    indexOf =0
    for i in fridge:
        if item.lower() == i.lower():
            return indexOf
        indexOf+=1
    return -1
#----------------------------------------------------------------------------------#
fridge =["meel", "vegetables","milk"]
item = input("Please enter what you need from the fridge :")
placeOfFood = whereIsMyFood(fridge, item)
#----------------------------------------------------------------------------------#
while placeOfFood < 0:
    print(-1)
    item = input("Please enter what you need from the fridge :")
    placeOfFood = whereIsMyFood(fridge, item)
#----------------------------------------------------------------------------------#
print(placeOfFood)
