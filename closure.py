




def parent_function(person,coins):
    # coins = 3
    
    def play_game():
        nonlocal coins
        coins -= 1
        
        if(coins >= 1):
            print("\n" + person + " has " + str(coins) + " left!")
        elif(coins == 1):
            print("\n" + person + " has " + str(coins) + " left!")
        else :
            print('\n' + person + " is out coins")
            
    return play_game
    

Noman = parent_function("Noman",3)
Hamza = parent_function("Hamza",4)

Noman()
Noman()

Hamza()

Noman()