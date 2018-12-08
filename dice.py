#import random
from random import randint
print ("Enter the lower limit")
a=int(input())
print ("Enter the largest number")
b=int(input())
print("type q to Quit or any other key/enter to continue")
while True:
    print (">>> "+str(randint(a, b))) #randint is generating random number between a and b
    if input() == 'q': #if 'q' is entered then come out of loop 
        break;
