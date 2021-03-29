class Main_character:
    def __init__(self, name, health=1000):
        self.name = name
        self.health = health
        
    def heal_up(self):
        while self.health < 500:
            self.health += 100
            print(F"********************\n{riven.name} uses a potion to restore 100 health.")
            return
        else:
            print(f"********************\n{riven.name} has too much health to use a potion!")
            return

    def take_damage(self, damage):
        self.health -= damage
        

    def view_stats(self):
        print(f"********************\nCharacter Name: {self.name}, the Exile\nAttack: 100\nHealth: {self.health}\n********************")

    def ultimate_ability(self):
        print(f"""
        Riven - "I can't lose...not like this...!!!"\n
        Riven summons a massive sword glowing with blue energy and fires an energy wave at Darius dealing 9999 damage!!!
        """)
        print("""
                           _
                          ( ((                                                   )>>))>>)                            
                           ) ))                                                     )>>))>>)
  .::.                    / /(                                                          )>>))>>)         
 'R .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._             )>>))>>)
(C ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>          )>>))))>)>>
 `3 `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''              )>>))>>)
  `::'                    \ \(                                                          )>>))>>)
                           ) ))                                                     )>>))>>)
                          (_((                                                   )>>))>>)\n
        Darius has 0 health remaining.
        *******************\n
        *******************\n\n
        Riven is victorious!!!\n\n
        *******************\n
        *******************
        """)
        exit()

riven = Main_character("Riven")

class Final_boss:
    def __init__(self, name, health=9999):
        self.name = name
        self.health = health
        
    def heal_up(self):
        self.health += 999

    def take_damage(self, damage):
        self.health -= damage

    def view_stats(self):
        print(f"********************\nCharacter Name: {self.name},the Hand of Noxus\nAttack: ???\nHealth: ???\n********************")

darius = Final_boss("Darius")

def battle():
    print(f"********************\n{riven.name} slashes {darius.name} with her blade!")
    riven.take_damage(200)
    darius.take_damage(100)
    print(f"{darius.name} takes 100 damage and has ??? health remaining.")
    print(f"{darius.name} swings his axe menacingly at {riven.name} dealing 200 damage!")
    print("Darius just smirks at Riven...\n********************")

def dodge():
    darius.heal_up()
    print(f"********************\n{riven.name} narrowly evades Darius' attack, however, Darius' recovers 999 health...")

def final_move():
    if riven.health <= 200:
        riven.ultimate_ability()
        exit()

def main_menu():
    final_move()
    message = int(input("""
    Darius is charging towards Riven! What do you do?\n
    1. Attack Darius with Riven's sword
    2. Dodge the incoming attack
    3. Use a potion
    4. Check on Riven's health
    5. Surrender
    """))
    print(message)
    while message != "x":
        if message == 1:
            battle()
            main_menu()
        elif message == 2:
            dodge()
            main_menu()
        elif message == 3:
            riven.heal_up()
            main_menu()
        elif message == 4:
            riven.view_stats()
            print(f"{darius.name} launches a surprise attack and deals 400 damage!!!")
            riven.take_damage(400)
            print(f"{riven.name} now has {riven.health} health remaining...")
            main_menu()
        elif message == 5:
            print("********************\nThere is no surrendering...!!!")
            main_menu()
        else:
            riven.take_damage(50)
            print("********************\nRiven takes 50 damage due to 'user error'. Please select a valid menu option.")
            main_menu()

print("""
                 ___====-_  _-====___
           _--^^^#####//      \\\#####^^^--_
        _-^##########// (    ) \\\##########^-_
       -############//  |\^^/|  \\\############-
     _/############//   (@::@)   \\\############\_
    /#############((     \\\//     ))#############\\
   -###############\\\    (oo)    //###############-
  -#################\\\  / VV \  //#################-
 -###################\\\/      \//###################-
_#/|##########/\######(   /\   )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
   `   `  `      `   / | |  | | \   '      '  '   '
                    (  | |  | |  )
                   __\ | |  | | /__
                  (vvv(VVV)(VVV)vvv)\n\n
                  Riven vs Darius\n\n
""")
riven.view_stats()
darius.view_stats()
main_menu()