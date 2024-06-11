import secrets
import getpass
from colorama import init, Fore, Style

def generate_secret_key(length=32):
    """Generates a random, URL-safe base64 encoded secret key.

    Args:
        length (int, optional): The desired length of the secret key in bytes. Defaults to 32.

    Returns:
        str: The URL-safe base64 encoded secret key.
    """
    return secrets.token_urlsafe(length)

# Initialize colorama
init()

# Generate a secure secret key (never print it)
secret_key = generate_secret_key()

# Get admin credentials from environment variables
admin_username = ('admin')
admin_password = ('admin')

# Maximum number of attempts
max_attempts = 3

# Allow the user to input credentials with feedback
for attempt in range(max_attempts):
    user_input_username = input("Username: ")
    
    # Check if the entered username is correct
    if user_input_username == admin_username:
        user_input_password = getpass.getpass("Password: ")
        
        # Check if the entered password is correct
        if user_input_password == admin_password:
            secret_key = generate_secret_key()
            print(f"""
{Fore.GREEN}10101010101010101010101010ABABABABAB1HGHGHGH101GH01GH0G1H0G1HG0H1GH0G1H1
**11D11F1A5S5ASD25S0101010ABABABABAB1HGHGHGH101GH01GH0G1H0G1HG0H1GH0G***
**|**|<II5ASG5SD5CS0101010ABABABABAB1HGHGHGH101GH01GH0G1H0G1HG0H1>|**|**
**|**|  **             {Fore.BLUE}Generating secret key...{Fore.GREEN}               **  |**|**
**|**|  [F101020151101Q|QW1|1010Q10101Q3399Q09011010101010Q10W>*] |**|**
**|**|  {Fore.YELLOW}*|*|*| **   Secret key generated successfully! ** *|*|*|  {Fore.GREEN}|**|**
**|**|  E4E5E45E8**         {Fore.RED}****WARNING****{Fore.GREEN}         **E4E5E45E8   |**|**
**|**|  ********************************************************  |**|**
**|**|  <-------------------------------------------------------  |**|**
**|**|  ********************************************************  |**|**
**|**|  Secret Key: {Fore.RED}{secret_key}{Fore.GREEN}   |**|**
**|**|  ********************************************************  |**|**
**|**|  ------------------------------------------------------->  |**|**
**|**|  ********************************************************  |**|**
**|**|  Q8Q8W8Z8**         {Fore.RED}****WARNING****{Fore.GREEN}         **Q1W1E1R1Z    |**|**
**|**|  ** Remember to store it securely and avoid                |**|**
**|**|  ** displaying it in code or logs.                         |**|**
**|**|<II5ASG5SD5CS0101010ABABABABAB1HGHGHGH101GH01GH0G1H0G1HG0H1>|**|**
**11D11F1A5S5ASD25S0101010ABABABABAB1HGHGHGH101GH01GH0G1H0G1HG0H1GH0G***
10101010101010101010101010ABABABABAB1HGHGHGH101GH01GH0G1H0G1HG0H1GH0G1H1  
{Style.RESET_ALL}
""")
            break 
        else:
            print(Fore.RED + "Wrong password. Please try again." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Wrong username. Please try again." + Style.RESET_ALL)
else:
    # If the loop completes without finding correct credentials after max_attempts
    print(Fore.RED + "Maximum attempts reached. Exiting..." + Style.RESET_ALL)
