#This is Prototype 1 for TalkBox


def parsing_excel (file_name):
    '''(str) -> (dict)
    Returns a dictionary of the phrases in the txt file
    '''
    f = open(file_name).readlines()
    my_dict = {}
    
    for i in range(len(f)):
        t = f[i]
        my_dict[i+1] = t
    return my_dict

def sentence(x, dictionary):
    '''(integer) -> (str)
    Returns the sentence that corresponds to that integer
    '''
    return (dictionary[x])


#main

simple_phrases = "Simple Phrases.txt"
talk = parsing_excel(simple_phrases)

home_devices = "Home Devices.txt"
home = parsing_excel(home_devices)



print("Please select a category")
print("1. Home Devices")
print("2. Simple Phrases")
print("Press space if you wish to exit")
choice = input()


if choice == '1':
    flag = True
    while flag:
        for i in range(1,len(home)+1):
            print (i, home[i])
        number = int(input("Please enter a number between 1-"+ str(len(home))+": "))
    
        if (number < 1) or (number > len(home)):
            print("Error: Please try again")
        else:
            flag = False
    print('\n')
    command = sentence(number, home)
    print (command)



elif choice == '2':
    flag = True
    while flag:
        for i in range(1,len(talk)+1):
            print (i, talk[i])
        number = int(input("Please enter a number between 1-"+ str(len(talk))+": "))
    
        if (number < 1) or (number > len(talk)):
            print("Error: Please try again")
        else:
            flag = False

    print('\n')
    say = sentence(number, talk)
    print (say)

    
else:
    print("Good bye :)")
    