#!/home/mamaah/development/PWG/bin/python3
#import random
import random 
#password generator
#random, min = 8 - 12 characters, max =32;
max_length = random.randint(8, 32)
# and must have  mixture of alphanumeric characters and special xters
#create a variable for the digits
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#creaate variable for lowercase xters
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#create variable for uppercase xters
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#create variable for special xters
special_characters = ['!', '@', '#', '$', '%','~', '^', '&', '*', '(', ')', '_', '+', '?', '/', '\\', '<', '|', '<', '>' ]
#combine the variables above to form a new list called Combined_list
combined_list = digits + lowercase + uppercase + special_characters
#randomly select xters from the combined_list upto to the max length minus 4
rand_digits = random.choice(digits)
rand_lowercase = random.choice(lowercase)
rand_uppercase = random.choice(uppercase)
rand_special = random.choice(special_characters)
#Combine the values from the 4 variable plus values selected from the combined list
password = rand_digits + rand_lowercase + rand_special + rand_uppercase
#Generate random passwords and convert into a string
print(max_length)
while len(password) != max_length:
    password = password + random.choice(combined_list)
print(password)