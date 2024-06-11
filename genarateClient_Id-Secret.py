# import string
# import random
# from colorama import init, Fore, Style

# def generate_client_id(length=32):
#   """Generates a random string resembling a client ID format."""
#   chars = string.ascii_uppercase + string.digits + string.ascii_lowercase + "-_"
#   return ''.join(random.choice(chars) for _ in range(length))

# def generate_client_secret(length=32):
#   """Generates a random string resembling a client ID format."""
#   chars = string.ascii_uppercase + string.digits + string.ascii_lowercase + "-_"
#   return ''.join(random.choice(chars) for _ in range(length))

# # CLIENT_SECRET = "your_testing_secret"

# # Example usage
# client_id = generate_client_id()
# client_secret = generate_client_secret()

# # print(f"Client ID: {client_id}")
# # print(f"Client Secret: {client_secret}")

# print(f"""
# {Fore.GREEN}-------------- BEGIN Client ID ------------------
# Client ID:  {Fore.CYAN}{client_id}{Fore.GREEN}
# --------------  END Client ID  ------------------
# """)

# print(f"""
# -------------- BEGIN Client Secret ----------------
# Client Secret:  {Fore.CYAN}{client_secret}{Fore.GREEN}
# --------------END Client Secret  ------------------
# {Style.RESET_ALL}
# """)



# =======================================================================================

import string
import random
from colorama import init, Fore, Style
import getpass


def generate_client_id(length=32):
    """Generates a random string resembling a client ID format."""
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase + "-_"
    return ''.join(random.choice(chars) for _ in range(length))


def generate_client_secret(length=32):
    """Generates a random string resembling a client ID format."""
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase + "-_"
    return ''.join(random.choice(chars) for _ in range(length))

# Maximum number of attempts
max_attempts = 3

# Allow the user to input credentials with feedback
for attempt in range(max_attempts):
    user_input_username = input("Username: ")

    # Check if the entered username is correct
    if user_input_username == "admin":  # Replace with actual username verification logic (e.g., database lookup)
        user_input_password = getpass.getpass("Password: ")

        # Check if the entered password is correct (replace with actual password verification logic)
        if user_input_password == "admin":  # Replace with actual password verification
            client_id = generate_client_id()
            client_secret = generate_client_secret()

# Example usage
# client_id = generate_client_id()
# client_secret = generate_client_secret()

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
