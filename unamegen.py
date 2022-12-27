import random
import string

def generate_username():
  # Choose a random length for the username
  username_length = random.randint(5, 10)
  
  # Generate a random username using lowercase letters and digits
  username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
  
  # Add the domain to the username
  username += "@egen.com"
  
  return username

# Generate a list of 5 random usernames
username_list = [generate_username() for _ in range(5)]
print(username_list)
