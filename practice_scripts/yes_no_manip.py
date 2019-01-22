# Copied from file_list.py. Need to just update everything

def textset():
    import os
    directory = input("Absolute path to check: ")
    dirmessage = directory + ' contains'
    print(dirmessage)
    for file in os.listdir(directory):
        print(file)
    catfile = input("Use which file? ")
    catfile = directory + '/' + catfile
    contents = open(catfile, 'r').read()
    print (contents)



while True:
    tagquestion = input('Would you like to add tags automatically \n')
    if tagquestion == '' or not tagquestion[0].lower() in ['y','n']:print('Please answer with yes or no!')
#        else:break
    if tagquestion[0].lower() == 'y': 
        textset()
        break
    if tagquestion[0].lower() == 'n': 
        print("Carrying on, then")
        break


print("That was fun, wasn't it?")
