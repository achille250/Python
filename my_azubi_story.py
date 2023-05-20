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
   place = input('Where do you live: ')
   
 # User provide different favourite course 
   while True:
     course = input('What is your favourite course so far or Press "done" to finish : ')
     if course=="done":
         break
     user_response.append(course)
  # Creating story template
   print(f"My name is {name_hold.upper()}.I live in {place.upper()} Here is my story: \n" )
   print(f"I am currently enjoying the Cloud Engineering course at Azubi Africa. It has been an incredible learning journey so far ")
   print(f"The instructors have been amazing ,I also want to thank all the fellow students who have been on this journey with me ")
  # Displaying favorite course
   print(f"My favorite course so far are : \n")
   for course in user_response:
    print(course.upper())
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


