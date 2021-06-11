import hashlib
import sys
import hmac
import binascii

passwordList = []
with open ('password.txt', 'r') as file:
    for line in file:
        currentPlace = line[:-1]
        passwordList.append(currentPlace)

if len(sys.argv) == 2:
    msg = sys.argv[1].encode()
    hashvalue = hashlib.md5(msg)
    print(hashvalue)
    print(hashvalue.hexdigest().upper())

if len(sys.argv) == 3:
    for i in range (len(passwordList)):
        msg=passwordList[i].encode()
        hashValue2 = hashlib.md5(msg)
        hashde=(hashValue2.hexdigest().upper())
        if str(hashde) == str(sys.argv[2]):
            print("password:"+passwordList[i])
            break
