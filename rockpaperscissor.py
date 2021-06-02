import random as random
print("welcome to rock paper scissor")
rps= ["rock","paper","scissor"]
compchoice=random.choice(rps)
def Logic():
     if userin==compchoice:
        print("Tie")
     elif userin=='rock' and compchoice=="paper":
        print("Computer wins")
     elif userin=='paper' and compchoice=="rock":
        print("You win")
     elif userin=='scissor' and compchoice=="paper":
        print("You win")
     elif userin=='paper' and compchoice=="scissor":
        print("Computer wins")
     elif userin=='rock' and compchoice=="scissor":
        print("You win")   
     elif userin=='scissor' and compchoice=="rock":
        print("Computer wins")



while True:
    
    userin= input("Enter your choice")
    print(userin)
    print(compchoice)
    Logic()
   


