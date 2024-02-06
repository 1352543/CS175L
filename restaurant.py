#CS175L
#Andrew Fisher
#Restaurant

vegetarian = False
vegan = False
gluten_free = False

response1 = input("Is anyone in your party vegetarian? ")
if response1 == "yes":
    vegetarian = True
elif response1 == "no":
    vegetarian = False

response2 = input("Is anyone in your party vegan? ")
if response2 == "yes":
    vegan = True
elif response2 == "no":
    vegan = False

response3 = input("Is anyone in your party gluten free? ")
if response3 == "yes":
    gluten_free = True
elif response3 == "no":
    gluten_free = False


print("Here are your restaurant choices:")    
if vegetarian:
    if vegan:
        if gluten_free or not gluten_free:
            print("Corner Café")
            print("The Chef's Kitchen")
    elif gluten_free:
        print("Main Street Pizza Company")
        print("Corner Café")
        print("The Chef's Kitchen")
    else:
        print("Mama's Fine Italian")
        print("Main Street Pizza Company")
        print("Corner Café")
        print("The Chef's Kitchen")
elif vegan: #vegetarian = no
        if gluten_free or not gluten_free:
            print("Corner Café")
            print("The Chef's Kitchen")
else: #vegan = no
    if gluten_free:
        print("Main Street Pizza Company")
        print("Corner Café")
        print("The Chef's Kitchen")
    else:
        print("Joe's Gourmet Burgers")
        print("Mama's Fine Italian")
        print("Main Street Pizza Company")
        print("Corner Café")
        print("The Chef's Kitchen")

