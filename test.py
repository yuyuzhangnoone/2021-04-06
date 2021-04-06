import hashlib
import sys



passwordlist = []
with open('passwd.txt','r') as filehandle:
    for line in filehandle:
        currentPlace = line[:-1]
        passwordlist.append(currentPlace)
#print(passwordlist)




def encrypt(self,msg):
    msgList = msg
    hashvalue=hashlib.sha256(msgList)
    print(hashvalue)
    print("")
    print(hashvalue.hexdigest().upper())
        
# def decrypt(self,msg):
        


if __name__ == '__main__':
    if len(sys.argv)>2:
        if sys.argv[1]=='-e':
            key=sys.argv[2]
            print(encrypt(sys.argv[2]))  
        # elif sys.argv[1]=='-d':
            # print(decrypt(sys.argv[2]))