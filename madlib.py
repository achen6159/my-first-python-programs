# This program starts a game where you control what it's about
#
# Annie Chen
# August 28, 2017


print("Let's play a game. Say yes or no.")
answr = input()
if answr == "yes":
    print("Ok, let's start")
    response = True

elif answr == "no":
    print("Ok, it's your lost.")
    response = False

else:
    print("Sorry, I don't understand")
    response = False
    
while response == True:
    print("Give me a noun")
    noun1=input()
    print("Ok, now give me a verb")
    verb1=input()
    print("Now give me another noun")
    noun2=input()
    print("Now give me an adjective")
    adj1=input()
    print("Give me another verb")
    verb2=input()
    print("Ok, give me another adjective")
    adj2=input()
    print("One day a " + adj1 + " " + noun1 + " " + verb1 + "." + " Then it made friends with a " + adj2 + " " + noun2 + " " + verb2 + ".")
    print("They were the best of friends and lived happily ever after.")
    response = False


   
          

