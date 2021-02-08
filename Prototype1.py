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

file_name = "Prototype1.txt"
r = parsing_excel("Prototype1.txt")

flag = True
while flag:
    for i in range(1,len(r)+1):
        print (i, r[i])
    number = int(input("Please enter a number between 1-"+ str(len(r))+": "))
    
    if (number < 1) or (number > len(r)):
        print("Error: Please try again")
    else:
        flag = False
    
t = sentence(number, r)
print (t)

