import random
from wind32com.client import Dispatch
  
print("\n              S T O N E     P A P E R     S C I S S O R     G A M E\n") 

# creating a speaking function for more good experience
def speak(str):
  speak = Dispatch("SAPI.SpVoice")
  speak.Speak(str)

while True:
  
# Rules of the game   
    print("""Enter your choice : 
    speak("Please have a look on instructions")
    a. Press '1' to select 'Stone'. 
    b. Press '2' to select 'Paper'.
    c. Press '3' to select 'Scissor'.\n""") 

# Take input from user 
    speak("Please enter your choice")
    user_choice = int(input("Enter YOUR choice: ")) 
  
# If user enters values other than 1,2 or 3
    while user_choice > 3 or user_choice < 1:
        speak("You have entered a wrong key, please check it..")
        user_choice = int(input("Enter valid input: ")) 
      
# Assigning numbers to the user's choices
    if user_choice == 1: 
        choice_name = 'Stone'
    elif user_choice == 2: 
        choice_name = 'Paper'
    else: 
        choice_name = 'Scissor'
    
    speak("Your choice is :, choice_name)
    print("YOUR choice is: ",choice_name) 
    print("\nNow, its COMPUTER'S turn.......") 

    computer_choice = random.randint(1, 3) 

    while computer_choice == user_choice: 
        computer_choice = random.randint(1, 3) 

# Assigning numbers to the computer's choices
    if computer_choice == 1: 
        computer_choicehoice_name = 'Stone'
    elif computer_choice == 2: 
        computer_choicehoice_name = 'Paper'
    else: 
        computer_choicehoice_name = 'Scissor'
          
    print("COMPUTER'S choice is: ",computer_choicehoice_name,"\n") 
    speak(f"Computer's choice is {computer_choicehoice_name}")
          
          
    print(choice_name," V/s ",computer_choicehoice_name) 

    if((user_choice == 1 and computer_choice == 2) or
      (user_choice == 2 and computer_choice ==1 )): 
        print("Paper wins !!! \n", end = "")
        speak("Paper wins !!!")
        result = "Paper"
          
    elif((user_choice == 1 and computer_choice == 3) or
        (user_choice == 3 and computer_choice == 1)): 
        print("Stone wins !!! \n", end = "")
        speak("Stone wins !!!")
        result = "Stone"
    else: 
        print("Scissor wins !!!\n", end = "")
        speak("Scissor wins !!!")
        result = "Scissor"

    if result == choice_name: 
        print("\nYOU WIN !!!\n")
        speak("YOU WIN !!!")
    else: 
        print("\nCOMPUTER WINS !!!\n")
        speak("COMPUTER WIN !!!")
          
    print("Do you want to play again? (y/n)") 
    ans = input() 
  
    if ans == 'n' or ans == 'N': 
        break

print("\n           T H A N K S     F O R     P L A Y I N G     ! ! ! ! !\n") 
