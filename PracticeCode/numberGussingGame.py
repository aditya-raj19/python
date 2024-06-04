import random
''' Build a Number guessing game, in which the user selects a range.
    Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
    Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses'''
s=int(input("Entert the Start of Range "))
e=int(input("Entert the End of Range "))
k=random.randrange(s,e)
print(k)
count=1
while(1):
    gn=int(input("Enter the number "))
    if(gn==k):
        break
    else:
        print("Wrong Guess Try Again")
        print("You have Used",count,"chance")
        count=count+1

print("You took ",count," chance To guess the number")


