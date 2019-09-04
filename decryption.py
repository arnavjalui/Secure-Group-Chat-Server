
#Imports
from Crypto.Cipher import AES
import base64
import os

#Functions
def decryption(encryptedString):

    '''

        @param Input: The encrypted string from the file
        @print  Output: The decrypted message

    '''

    PADDING = '{'
    DecodeAES = lambda c,e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    file = open('key.txt','r').read()
    key = file
    cipher = AES.new(key)
    decoded = DecodeAES(cipher, encryptedString)
    # print "Original message was " + decoded
    return decoded

