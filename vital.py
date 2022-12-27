import random
import string

def generate_username_and_password():
  # Open the inuse.txt file in read-only mode
  with open("inuse.txt", "r") as f:
    # Read the list of usernames from the file
    inuse_usernames = f.read().splitlines()
  
  # Generate a random username until we find one that is not in use
  username = None
  while username is None or username in inuse_usernames:
    # Choose a random length for the username
    username_length = random.randint(5, 10)
    
    # Generate a random username using lowercase letters and digits
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    
    # Add the domain to the username
    username += "@egen.com"
  
  # Choose a random length for the password
  password_length = random.randint(8, 12)
  
  # Generate a random password using lowercase letters, uppercase letters, and digits
  password = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=password_length))
  
  return (username, password)

# Generate a list of 5 random usernames and passwords
credentials_list = [generate_username_and_password() for _ in range(5)]
print(credentials_list)
