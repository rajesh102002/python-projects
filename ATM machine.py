import time

print('please insert atm card')

#for card processing

time.sleep(5)

password = 1234

#use account balance
balance =1000

#taking atm pin from user
user_pin = int(input("Enter your pin numper:"))
#checking pin is valid or not

if password == user_pin:
    #loop will run user get free
  while True:
      print("=============================================")
      print(""""
            1 == balance
            2 == deposit
            3 == withdraw
            4 == exit
            """)
      print("==================================================")
      try:
          #taking an option from user
          option = int(input("please enter your choice:")) 
             
        #option 1  
          if option ==1:
              print("==================================================")    
              print(f"your current balance{balance}")
              print("==================================================")    
        #option 2
          elif option ==2:
              deposit = int(input("pls enter deposit amount"))
              balance=balance+deposit
              print("==================================================")    
              print(f"{deposit} is credited to your account")      
              print(f" your updated balance {balance}")
              print("==================================================")   
              
        #option 3       
          elif option == 3:
              withdraw = int(input("do shout have how many mony"))
              balance= balance - withdraw
              print("==================================================")    
              print(f"{withdraw} is depited from your account") 
              print(f" your updated balance {balance} ")
              print("==============================================")
        # stop program
          elif option == 4:
              break         
      except:
          print("pls select correct option")  
else:
   print('wrong pin numper pls try again')    