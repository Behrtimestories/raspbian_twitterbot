#Some functional fun!
def lencheck():
    if len(message) < 280:
        print("Text is under 280 characters.")
        print(message)
#        break
    else:
        print("Over posting limit, sorry. Try again?\n")
        tweeter()
#Prompt for message
#message = input("What's on your mind? ")
#Add some additional tags?
#def tweeter():
    message = input("What's on your mind? ")
    while True:
        tagquestion = input("Would you like to add some tags? (y/n)\n")
        if tagquestion == "" or not tagquestion[0].lower() in ["y","n"]:print("Please answer with yes or no!")
                    #        else:break
        if tagquestion[0].lower() == "y": 
            taglist = input("No, that's fine. Hash... just hashtag it.\n")
            message = message + taglist
            break
        if tagquestion[0].lower() == 'n':
            print("Carrying on, then")
            break

#prompt for message
#message = input("What's on your mind? ")

#tweeter()

if len(message) < 280:
    print("Text is under 280 characters.")
    print(message)
                    #        break
else:
    print("Over posting limit, sorry. Try again?\n")
#    tweeter()
#lencheck(message)
print("That was fun!")
#Print Tweet/confirmation
#print(message)
