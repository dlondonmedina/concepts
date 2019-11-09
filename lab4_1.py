def is_even():
   # Notice, this will give us an error if we don't enter an integer
   # in Everyday Coding, we'll learn how to catch errors like this.
   user_data = int(input("Please give me an integer. "))
   out = None
    
   # Create a conditional that sets out to True if the user enters
   # an even integer and False if the user enters an odd integer.
   if user_data % 2 == 0:
      out = True
   else:
      out = False 
   
   # This is for the test.
   return out 

def multi_condition():
   # Notice, this will give us an error if we don't enter an integer
   # in Everyday Coding, we'll learn how to catch errors like this.
   user_data = int(input("Please give me an integer. "))

   # Now evaluate the user_data again and have several conditions
   # if the value is zero, print "Don't be such a zero!"
   # if the value is positive and odd, print "Positively odd!"
   # if the value is positive and even, print "Even Steven!"
   # if the value is negative and odd or even, print "Negative Nelly!"
   # remember, with multiple conditions you can use if, elif, elif, else
   if user_data == 0:
      print("Don't be such a zero!")
   elif user_data < 0:
      print("Negative Nelly!")
   elif user_data % 2 == 0:
      print("Even Steven!")
   else:
      print("Positively odd!")

   return None


def is_underage():
   # Prompt the user for their age and store it to a variable. Don't
   # forget to convert the input to an integer.
   age = int(input("How old are you? "))

   # Set up a conditional with four cases
   # if the age is equal to or above 21, 
   # print "You may drink, smoke, and drive if you wish!"
   # if the age is equal to or above 18 but less than 21, 
   # print "You may smoke and drive!"
   # if the age is equal to or above 16 but less than 18,
   # print "You may drive!"
   # if the age is less than 16, 
   # print "Enjoy your bike, kid!"
   
   if age >= 21:
      print("You may drink, smoke, and drive if you wish!")
   elif age >= 18:
      print("You may smoke and drive!")
   elif age >= 16:
      print("You may drive!")
   else:
      print("Enjoy your bike, kid!")

   # So the tests fail and they don't throw errors
   return None

def countdown():
   # Use a loop to print a countdown from 10 to zero with
   # one number on each new line. If you do not use a loop
   # you will not get points for this problem.
   count = 10
   while count >= 0:
      print(count)
      count -= 1
   
   # So the tests fail and they don't throw errors
   return None

def guessing_game(num):
   # This is a guessing game. I have set up a parameter that will be
   # a random integer that your user will have to try to guess.
   # To use num in your condition, you should write something like
   # 
   # if user_input == num: 
   #    
   # You should give your user at most 10 guesses to guess
   # the number. If the guess is too high or too low, you should tell 
   # them "Too High!" or "Too Low!" with the print statement.
   # If they guess the number, you should tell them "You win!"
   # otherwise, if they run out of guesses, tell them, "You lose!"
   # If they want to, your condition should also check for "q" and 
   # if the user enters that the program should exit, saying 
   # "Goodbye, quitter!"
   # No, it's not a very nice program. 
   count = 10
   while count > 0:
      user_input = input("Guess a number, please! ")
      if user_input == "q":
         print("Goodbye, quitter!")
         return None 
      
      user_input = int(user_input)
      if user_input == num:
         print("You win!")
         return None
      elif user_input > num:
         print("Too High!")
      else:
         print("Too Low!")
      count -= 1

   print("You Lose!")

   # So the tests fail and they don't throw errors
   return None