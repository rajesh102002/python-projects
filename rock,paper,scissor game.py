import random

user =0
computer =0

options = ["rock","paper","scissor"]

while True:
    user_type =input("rock/paper/scessor or exit:").lower()
    
    if user_type == "exit":
        quit()
        
    if user_type not in options:
        continue
    
    
    random_numper = random.randint(0,2)
    comuter_type = options[random_numper]
    print("computer",comuter_type)
    
    if user_type == "rock" and comuter_type == "scissor":
        print("you win")
        user+=1
        
    elif user_type == "paper" and comuter_type == "rock":
        print("you win") 
        user+1
        
    elif user_type == "scissor" and comuter_type == "papper":
         print("you win")
         user+1
    else:
        print("you lost")
        computer+=1
        
    print("you won ",user)
    print("computer won",computer)            
        
    