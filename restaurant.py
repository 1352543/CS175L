#CS175L
#Andrew Fisher
#Restaurant

search = "yes"

while search == "yes":

    vegetarian = False
    vegan = False
    gluten_free = False

    response1 = input("Is anyone in your party vegetarian? (enter 'yes' or 'no') ")
    if response1 == "yes":
        vegetarian = True

    response2 = input("Is anyone in your party vegan? (enter 'yes' or 'no') ")
    if response2 == "yes":
        vegan = True

    response3 = input("Is anyone in your party gluten free? (enter 'yes' or 'no') ")
    if response3 == "yes":
        gluten_free = True

    print("Here are your restaurant choices:") #Determines restaurant   
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

    search = input("Enter 'yes' if you would like to do another restaurant search (enter 'no' to end) ")

