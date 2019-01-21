
# import the important bits we'll be using. In this case, just the os module
import os

#Set up the basic variables
#directory = "/home/pi/scripts/twitter/message_files"
directory = input("Absolute path to check: ")
dirmessage = directory + ' contains'

# List all objects in the directory path
print(dirmessage)
for file in os.listdir(directory):
#    if file.endswith(".tags"):
#        print(os.path.join(directory, file))
#        print (dirmessage)
        print(file)

# Prompt for the file whose contents need to be printed
catfile = input("Use which file? ")
catfile = directory + '/' + catfile

with open(catfile, 'r') as fin:
    print(fin.read(), end="")
