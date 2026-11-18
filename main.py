TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {"bob": "123", 
         "ann": "pass123", 
         "mike": "password123", 
         "liz": "pass123"}

input_username = input("Enter username: ")
if input_username in users:
    input_password = input("Enter password: ")
    if users[input_username] == input_password:
        print(f"Welcome to the application, {input_username}!")
        print(f"We have {len(TEXTS)} texts to be analyzed.")
        text_choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select:" )
        if text_choice.isdigit() and 1 <= int(text_choice) <= len(TEXTS):
            print(f"There are {len(TEXTS[int(text_choice)-1].split())} words in the selected text. ")
            print(f"There are {sum(1 for word in TEXTS[int(text_choice)-1].split() if word.istitle())} titlecase words. ")
            print(f"There are {sum(1 for word in TEXTS[int(text_choice)-1].split() if word.isupper())} uppercase words. ")
            print(f"There are {sum(1 for word in TEXTS[int(text_choice)-1].split() if word.islower())} lowercase words. ")
            print(f"There are {sum(1 for word in TEXTS[int(text_choice)-1].split() if word.isnumeric())} numeric strings. ")
            print(f"The sum of all the numbers in the text is: {sum(int(word) for word in TEXTS[int(text_choice)-1].split() if word.isnumeric())} ")
            print("--------------------------------")            
            print("LEN | OCCURRENCES | NR.")
            print("--------------------------------")

            delky_slov = {}

            for slovo in TEXTS[int(text_choice)-1].split():
                delky_slov[len(slovo)] = delky_slov.get(len(slovo), 0) + 1

            for delka, cetnost in sorted(delky_slov.items()):
                print(f"{delka:>3} | {'*' * cetnost:<{max(delky_slov.values())}} | {cetnost:>3}")
        else:
            print("Invalid selection. Please enter a number between 1 and 3. Terminating the program. Please try again.")
    else:
        print("Incorrect password. Access denied.")
else:
    print("Username not found. Access denied.")





