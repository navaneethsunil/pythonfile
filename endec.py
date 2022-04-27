# Python program to be called with 3 command line arguments
# First parameter = Operation (decrypt/encrypt)
# Second parameter = String to be encrypted/decrypted
# Thrid Parameter = Password used for the encrypt/decrypt operation

# Please pip install cryptocode module before running the program

import sys
import cryptocode

operation = sys.argv[1]
str = sys.argv[2]
passwd = sys.argv[3]

if operation == 'encrypt':
        str_encoded = cryptocode.encrypt(str,passwd)
        print(str_encoded)
elif operation == 'decrypt':
        str_decoded = cryptocode.decrypt(str, passwd)
        print(str_decoded)
else:
        print("Wrong Operation Selected!")
