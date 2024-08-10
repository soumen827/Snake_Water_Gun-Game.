import random
# project 1
computer = random.choice([-1,0,1])
youstr = input("Enter your choice:")
youDict = {"s":1, "w":-1,"g":0}
reverseDict ={1:"Snake",-1:"Water",0:"Gun"}
you = youDict[youstr]
print(f" you chose{ reverseDict[you]}\n computer chose { reverseDict[computer]}")

if(computer==you):
    print("its Draw")

else:
    if( computer==-1 and you ==1):
        print("You win!")
    elif( computer==-1 and you==0):
        print("You lose!")
    elif(computer==1 and you==-1):
        print("You lose!")
    elif(computer==1 and you == 0):
        print("You Win!")
    elif( computer==0 and you==1):
        print("YOu lose!")
    elif(computer==0 and you==-1):
        print("You win!")

    else:
        print("Somthing went wrong!")


