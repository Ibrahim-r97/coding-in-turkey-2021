def validateRecipe(fridge, ingredients):
    
    count = 0  # count of things that chef is need it and it's in fridge
    for i in ingredients: # loop on ingredients items
        for f in fridge: # loop on fridge items
            if i == f: # check if the item in ingredients is in fridge
                count += 1
    return count
#----------------------------------------------------------------------------------#

# define variable
fridge =['onion', 'banana', 'lettuce', 'olives'] # item in fridge
x=0
item = ""
ingredients = []

# inpute the things that the chef need it
num = input("Please enter the number of things that you need : ")

print("Please enter what you need from the fridge :")
while x < int(num):
    item = input()
    ingredients.append(item)
    x += 1

# Check if all things he need it in fridge
if validateRecipe(fridge, ingredients) == len(ingredients):
    print("true")
else:
    print("false")

