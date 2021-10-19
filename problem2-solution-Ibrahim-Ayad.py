def validateRecipeWithQuantity(fridge, ingredients):
    
    count = 0  # count of things that chef is need it and it's in fridge
    for i in fridge.keys(): # loop on ingredients items
        for f in ingredients.keys(): # loop on fridge items
        
            if i == f and ingredients[f] <= fridge[i]: 
                count += 1
    return count
#----------------------------------------------------------------------------------#

# define variable
# ingredients = {'tomato': 1, 'onion': 4};
fridge = {'tomato': 1, 'onion': 3};
x=0
itemKey = ""
itemNum = ""
ingredients = {}

# inpute the things that the chef need it
num = input("Please enter the number of things that you need from the fridge : ")

while x < int(num):
    print("Please enter what you need from the fridge :")
    itemKey = input()
    print("Please enter howmany " + itemKey + " you need from the fridge :")
    itemNum = input()
    ingredients[itemKey] = int(itemNum)
    x += 1

# Check if all things he/she needs it in fridge
if validateRecipeWithQuantity(fridge, ingredients) == len(ingredients):
    print("true")
else:
    print("false")

