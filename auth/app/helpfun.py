import secrets
import hashlib


# Generate a 5-digit random number as a string
def otp (length):
    random_number = ''.join(secrets.choice('0123456789') for _ in range(length))
    return random_number



def hash(input):


    sha1 = hashlib.sha1()

    sha1.update(input.encode('utf-8'))
    hash_result = sha1.hexdigest()
    return  hash_result




def getdata(request, dict ):
    store =[]
    for i in dict:
        store.append(request.POST[i])
    return store

