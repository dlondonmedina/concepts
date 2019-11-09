# Write a function called divisible_by_7. 
# This function must take an integer as a parameter.
# This function must return True if the passed integer
# is divisible by 7 or false if not.
# Note, you should not prompt the user for input. 
def divisible_by_7(num):
   
   if num % 7 == 0:
      return True 
   else:
      return False


# Write a function called compare_it that takes two parameters. 
# You should first test if both parameters are integers.
# If not, return False
# Then you should test if the parameters are equal.
# If they are not, return False
# Finally, test if the parameters are greater than zero.
# If they are not, return False.
# If all of these tests pass, return True.
def compare_it(num1, num2):
   if not isinstance(num1, int) or not isinstance(num2, int):
      return False 

   if not num1 == num2 or num1 <= 0 or num2 <= 0:
      return False 
   
   return True

# Write a function called keyword_counter that takes three parameters
# Parameter one should be a list of words.
# The second should be a Boolean
# The third should be either a string or a filename
# The first parameter is your list of keywords.
# The second parameter if set to True means that the third parameter is a string
# The second parameter if set to False means that the third parameter is a filename
# In both cases, you will need to read a string and count occurrences of each
# keyword in that string. If the third parameter is a string, you can use that
# directly. If it is a filename, then you need to read the contents of a file
# into a string first. Then search for occurrences.
# Your function must return a dictionary with the keywords as the key and the 
# count of occurrences of that keyword as the value. 
# Since this is tricky, I've given you the code to read from a file that you'll
# need to include in your function.
# NOTE: Your test should not be case sensitive so if
# one of the words is "fish" your function should count 
# "fish", "Fish", "FISH" or any other combination of 
# capitalization as an occurrence. 
# file_name = "test6_1.txt" # DELETE THIS LINE before you build the function.
# with open(file_name, "r") as f:
#    text = f.read().replace("\n", " ")
def keyword_counter(words, is_string, text):
   if not is_string:
      with open(text, 'r') as f:
         text = f.read().replace("\n", " ")
   
   text = text.lower()
   out = {}

   for word in words:
      out[word] = text.count(word)

   return out   

