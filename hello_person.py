def hello(name,lang):
    greetings = {
        'English' : 'Hello',
        'French' : 'Bonjour',
        'Italia' : 'Ciao',
    }
    msg = f'{greetings[lang]} {name}!'
    print(msg)

if __name__ == "__main__":
    
    import argparse

    parser = argparse.ArgumentParser(
        description = "Providing personal greetings"
    )

    parser.add_argument(
        "-n" , "--name" , metavar='name',
        required=True , help="please enter name of person to greetings"
    )
    
    parser.add_argument(
        '-l' , '--lang' , metavar='language' ,
        required=True , choices=['Enlish','French','Italia'],
        help="Here Is the provided langauge for greetings",
    )

    
    args = parser.parse_args()

        
    hello(args.name,args.lang)