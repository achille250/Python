# Story Teller Program
print("************************************************")
print ("AZUBI AFRICA CLOUD ENGINEERING")
print("************************************************")
print ('WELCOME TO MY STORY')
print("************************************************")
while True:
 # Users provide the name and the place
   user_response = []
   name_hold = input('What is your name: ')
   print(" You are welcome, " f'{name_hold.upper()}. You are about to embark on a thrilling adventure ')
   #place = input('Where do you live: ')
   
 # User provide different favourite course 
   while True:
     country = input('Which country are you from: ')
     city = input('What city do you live in: ') 
     institute = input('What is the name of the training Institution? ')
     course = input('What course are you being trained for? ')
     duration = input('What is the duration of the program? ')
     testify = input('In one word, What can you say about their training: ') 
     user_end = input('Please type DONE: ')
     break
     user_response.append(user_end)

  # Creating story template
   print('\n')
   print("************************************************")
   print(f"""My name is {name_hold.upper()}.I live in {city.upper()}, {country.upper()}. 
I am currently running a {course} training program at {institute.upper()}.
{institute.upper()} provides a comprehensive {duration} training which prepares me for job search, resume building not leaving out the core technical skills for {course}.
The training is {testify}.""")

   print("************************************************")
   print("THE END")
   print("************************************************")
   # creating the option to play again
   while True:
        play_again=input ('Do you want to play again yes/no : ')
        if play_again.lower()=="yes" or play_again.lower()=='no':
          break
        else:
         print("Invalid Input. Please enter 'yes' or 'no' : ")
   if play_again.lower()=='no':
       break        
   # creating the option to save/share
   while True:
      save_story = input('Do you want to save/share or exit: ')
      if save_story.lower() == "save" or save_story.lower() == "share" or save_story.lower() == "exit":
        break
      else:
          print("Invalid input. Please enter 'save', 'share', or 'exit'.")
          
   if save_story.lower() == "save":
        print('Story saved')
   elif save_story.lower() == "share":
         print('Story shared')
   elif save_story.lower() == "exit":
        break


