import string
import random
from colorama import init, Fore, Style

def generate_client_id(length=32):
  """Generates a random string resembling a client ID format."""
  chars = string.ascii_uppercase + string.digits + string.ascii_lowercase + "-_"
  return ''.join(random.choice(chars) for _ in range(length))

def generate_client_secret(length=32):
  """Generates a random string resembling a client ID format."""
  chars = string.ascii_uppercase + string.digits + string.ascii_lowercase + "-_"
  return ''.join(random.choice(chars) for _ in range(length))

# CLIENT_SECRET = "your_testing_secret"

# Example usage
client_id = generate_client_id()
client_secret = generate_client_secret()

# print(f"Client ID: {client_id}")
# print(f"Client Secret: {client_secret}")

print(f"""
{Fore.GREEN}-------------- BEGIN Client ID ------------------
Client ID:  {Fore.CYAN}{client_id}{Fore.GREEN}
--------------  END Client ID  ------------------
""")

print(f"""
-------------- BEGIN Client Secret ----------------
Client Secret:  {Fore.CYAN}{client_secret}{Fore.GREEN}
--------------END Client Secret  ------------------
{Style.RESET_ALL}
""")