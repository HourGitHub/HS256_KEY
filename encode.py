import jwt
import random
import string


# Replace these with your actual data
secret_key = "RPcoQ6rczfR4Im6ZujSPbj3aL5lxd29rEf4UfhnjyMQ"  # This should be a long, random string
payload = {
    "TxnRef": "202406110933",
    "AgentID": "TESTING",
    "SecretCode": "TEST@123",
    "FirstNameEN": "PHO",
    "LastNameEN": "KEANGHOUR",
    "DateofBirth": "01012020",
    "Gender": "M",
    "Phone_Number": "12345678",
    "CARD INFO": {
        "ID_Number": "10234567",
        "ID_IssueDate": "20221211",
        "ID_ExpireDate": "20251111",
        "National": "KH",
        "Photo": "Base64",
        "Signature_Photo": "Base64",
        "Data": "",
    },
}

# # Random Data for Testing 
# payload = {
#   "TxnRef": f"202406{str(random.randint(10, 29))}{random.randint(10, 29)}{random.randint(1000, 9999)}",  # Generate random transaction reference
#   "AgentID": f"AGENT-{random.randint(100, 999)}",  # Generate random agent ID
#   "SecretCode": f"SECRET-{''.join(random.choices(string.ascii_uppercase + string.digits, k=8))}",  # Generate random alphanumeric secret code
#   "FirstNameEN": random.choice(["John", "Jane", "David", "Lisa", "Michael"]),  # Random first name
#   "LastNameEN": random.choice(["Smith", "Johnson","Williams", "Brown", "Jones"]),  # Random last name
#   "DateofBirth": f"{random.randint(1970, 2005)}-{random.randint(1, 12)}-{random.randint(1, 28)}",  # Generate random date of birth
#   "Gender": random.choice(["M", "F"]),  # Random gender
#   "Phone_Number": f"+855{random.randint(10, 99)}{random.randint(100000, 999999)}",  # Generate random Cambodian phone number
#   "CARD INFO": {
#     "ID_Number": f"{random.randint(10000000, 99999999)}",  # Generate random ID number
#     "ID_IssueDate": f"{random.randint(2010, 2023)}-{random.randint(1, 12)}-{random.randint(1, 28)}",  # Generate random ID issue date
#     "ID_ExpireDate": f"{random.randint(2025, 2035)}-{random.randint(1, 12)}-{random.randint(1, 28)}",  # Generate random ID expire date
#     "National": "KH",  # Keep national as KH (Cambodia)
#     "Photo": "Base64PhotoDataHere",  # Replace with actual Base64 encoded photo data if needed
#     "Signature_Photo": "Base64SignatureDataHere",  # Replace with actual Base64 encoded signature photo data if needed
#     "Data": "",  # Can be left empty or filled with additional data
#   },
# }

encoded_jwt = jwt.encode(payload, secret_key, algorithm="HS256")
# print(f"JWT Bearer: {encoded_jwt}")

print(f"""
----------------  BEGIN JWT Bearer ------------------\n
{encoded_jwt}
\n--------------  END JWT Bearer  --------------------
""")
