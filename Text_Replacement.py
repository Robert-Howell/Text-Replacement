   #This function will take a string with the unwanted "..."
   #And replace it with a ","

   #The function to replace the characters

def text_replace(bad_string):
    good_string = bad_string.replace("...", ", ")
    return good_string


   #Ask for the input, turn it into string, and print the result

annoying_string = str(input("What is the message?"))

print(text_replace(annoying_string))


   #Wish List: Pull the string from a file of some sort
