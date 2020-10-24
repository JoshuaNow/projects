class Hero:
    def __init__(self, name, position, health, power = 1):
        self.name = name
        self.health = 1
        self.power = power
        self.health = health
        self.position = position #[0,-5]  #I want a 5*6 grid with 120 blocks on the grid 

    def get_hit(self, power):
        self.health = self.health - power
    
    def move(self, dir):
        if dir == "up":
            self.position = [self.position[0], self.position[1]-1]
        elif dir == "down":
            self.position = [self.position[0], self.position[1]+1]
        elif dir == "left":
            self.position = [self.position[0]-1, self.position[1]]
        elif dir == "right":
            self.position = [self.position[0]+1, self.position[1]]
    

class bad_guy(Hero):
    def __init__(self , name, position , health = 10, power = 2):
        






name = input("What is your name little boy?"
print(f"It's okay {name} I know you are scared but we will get thru this.")
print("Just look for both keys without running into the bad guys, and we can escape.")











#thinking about doing a "scary game where the player is trying to make it to the safe place, because there are ghoust or enemies move around looking for you and if you 
# make it to the same coordinate then you lose. "


