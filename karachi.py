

from random import choice


capital = "Islamabad"

bird = "Parrot"

flower = "Rose"

song = "Home on the Range"

def randomFunFacts() :
    funFacts = [
        "Karachi is the largest city in Pakistan.",
        "he name Karachi derives from the Sindhi words 'Kari' and 'Bandar'.",
        "It is known for its bustling port.",
        "Karachi is a melting pot of cultures.",
    ]
    
    index = choice("0123")
    
    print(funFacts[int(index)])
    
    
if __name__ == "__main__":
    randomFunFacts()
    

