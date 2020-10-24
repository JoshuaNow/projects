#We can start off by defining a dictionary that holds out charactars attributes.

dog = {
    "name" : "Rocky",
    "fullness" : 50,
    "happiness" : 20,
}


# Now are going to define functions that increase the pets attribute levels.

def feed_pet(pet):
    pet["fullness"] += 10

def play_with_pet(pet):
    pet["happiness"] += 10

#now we are creating a way for the levels to decrease by using more functions, they are currently still called functions because
#they are now inside a class, if they were inside a class it would be called a method.
def get_hungry_and_mopey(pet):
    pet["fullness"] -= 5
    pet["happiness"] -= 5


#Now we are going to going to tell the user to interact with the pet by using a while loop 

while True:
    
        print("""
    %s's stats:
    Fullness: %d
    Happiness: %d
    """ % (dog["name"], dog["fullness"], dog["happiness"]))
     #   try: 
        choice = (input("""
    1. Feed dog
    2. Play with dog
    3. Do nothing
    """))
            # except ValueError:
    #     print("please use a number from the menu.")  
    

        if choice == "1":
            feed_pet(dog)
        elif choice == "2":
            play_with_pet(dog)
        # elif choice == 3:
        else:
            pass
        

        if dog["fullness"] == 0:
            False

        get_hungry_and_mopey(dog)
   
    ######### how do use the try and except properly here.

# this is how you create a game without the use of a classes
