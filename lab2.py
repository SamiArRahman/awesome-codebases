import random

def main():
    try:
        weapons = ["Fist","Knife","Club","Gun","Bomb","NuclearBomb"]
        weaponRoll = random.randint(1,6)
        print(f"You rolled:  {weaponRoll}")

        hero_strength = 0 
        total_strength = hero_strength + weaponRoll
        print(f"Your strength is now: {total_strength}")

        weapon_select = weapons[weaponRoll - 1]
        print(f"Your weapon is: {weapon_select}")
    
        if weaponRoll <= 2:
         print("You rolled a weak weapon, friend")
        elif weaponRoll <= 4:
         print("Your weapon is meh")
        else:
         print("Nice weapon friend")
        if weapon_select != "Fist":
         print("Thank goodness you didn't roll the Fist...")
        return total_strength, weapon_select
    except ValueError as e:
     print(f"Error: {e}")
if __name__ == "__main__":
 main()


 
    



    





   


