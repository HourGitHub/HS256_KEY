import jwt

# Replace with the encoded JWT from the previous step
encoded_jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJUeG5SZWYiOiIyMDI0MDYxMDI4NTgwOCIsIkFnZW50SUQiOiJBR0VOVC02OTAiLCJTZWNyZXRDb2RlIjoiU0VDUkVULUNXUlhLUFRIIiwiRmlyc3ROYW1lRU4iOiJMaXNhIiwiTGFzdE5hbWVFTiI6IlNtaXRoIiwiRGF0ZW9mQmlydGgiOiIxOTk5LTItNCIsIkdlbmRlciI6IkYiLCJQaG9uZV9OdW1iZXIiOiIrODU1OTY1OTU5ODMiLCJDQVJEIElORk8iOnsiSURfTnVtYmVyIjoiOTI1NDQ5MzEiLCJJRF9Jc3N1ZURhdGUiOiIyMDIyLTExLTIwIiwiSURfRXhwaXJlRGF0ZSI6IjIwMzUtOC0yMyIsIk5hdGlvbmFsIjoiS0giLCJQaG90byI6IkJhc2U2NFBob3RvRGF0YUhlcmUiLCJTaWduYXR1cmVfUGhvdG8iOiJCYXNlNjRTaWduYXR1cmVEYXRhSGVyZSIsIkRhdGEiOiIifX0.0Dt-lEAH4sCXjNIt9KZgjfnRW_4qJq6uSct9Y81Q7mk"

# Replace with your actual secret key
secret_key = "RPcoQ6rczfR4Im6ZujSPbj3aL5lxd29rEf4UfhnjyMQ"

# try:
#   decoded_payload = jwt.decode(encoded_jwt, secret_key, algorithms=["HS256"])
#   print(decoded_payload)
# except jwt.exceptions.DecodeError as e:
#   print(f"Error decoding JWT: {e}")
 

try:
    decoded_payload = jwt.decode(encoded_jwt, secret_key, algorithms=["HS256"])
    print(f"""
-------------- BEGIN Decoded_payload ------------------\n
{decoded_payload}
\n--------------  END Decoded_payload  ------------------
""")
except jwt.exceptions.DecodeError as e:
  print(f"Error decoding JWT: {e}")