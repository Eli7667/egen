import random
import string

def generate_email():
  # Choose a random length for the username
  username_length = random.randint(5, 10)
  
  # Generate a random username using lowercase letters and digits
  username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
  
  # Choose a random domain from a list of popular domains
  domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'aol.com', 'hotmail.com']
  domain = random.choice(domains)
  
  # Create the email address by combining the username and domain
  email = f"{username}@{domain}"
  
  return email

# Generate a random email
random_email = generate_email()
print(random_email)
