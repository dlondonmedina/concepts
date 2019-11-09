def sums():
   
   # Initialize a variable called first_sum and store the sum of 
   # 2 and 2
   first_sum = 2 + 2 

   # Store to first_sum the value of first_sum times 10
   first_sum = first_sum * 10

   # Initialize a variable called secret and assign it the value 
   # of first_sum plus 2
   secret = first_sum + 2
   return secret

def string_manip(first_name):

   # Initialize a variable called name and assign it the 
   # parameter.
   name = first_name

   # Use builtin string functions and slices to replace None with 
   # the appropriate manipulation of your name. I've done the first one.
   all_caps = name.upper()
   all_lowercase = name.lower()
   first_five_letters = name[:5]
   last_two_letters = name[-2:]

   return [all_caps, all_lowercase, first_five_letters, last_two_letters]

def greeter_bot():

   # Use the input() function to prompt the user for their name.
   # Then assign the value to a variable called name and print a greeting.
   # I have started it for you, but you need to modify the input and 
   # print functions.
   # Hint: to get the test to pass, the greeting should be "Hello, input name!"
   name = input("Hi, friend! What is your name? ")
   print("Hello, {}!".format(name))


def temp_calculator():

   # Write code that prompts the user for a temperature in degrees
   # fahrenheit and prints the equivalent temperature in degrees celsius.
   # The formula is C = (F - 32) * (5/9). 
   temp_f = float(input("What is the temperature in Fahrenheit? "))
   temp_c = (temp_f - 32) * (5/9)
   print(temp_c)

def equitable_bill_splitter():
   
   # Read the following code and add comments to each line explaining what
   # it does. To write a comment, begin the line with an octothorpe (hashtag, #)
   # Ask for a count of people from the user.
   people = int(input("How many people are paying? "))
   salaries = []
   total = 0
   
   for i in range(people):
      sal = int(input("What is the salary of person {}?".format(i+1)))
      total += sal
      salaries.append(sal)
   
   total_bill = int(input("How much is the bill? "))
   
   for j in range(len(salaries)):
      print("Person {} should pay ${}\n".format(j + 1, round((total_bill * (salaries[j]/total)), 2)))
