#Imports
from Crypto.Cipher import AES
import base64
import os
from decryption import decryption

#Functions

#Function to decrypr message
def decrypt():
	mess_file = open('message.txt','r')
	mess_file = mess_file.read()
	print "Read string : " + mess_file
	decryption(mess_file)



#Function to write to a file.
def fileWrite(filename,text):

    '''

        @param Input: The filename in which the given text is to be written
        @none  Output: Text is written in the file.

    '''


    file = open(filename,'w')
    file.write(text)
    file.close

#Function to encrypt a text.
def encryption(privateInfo):

    '''

        @param Input: The message which is to be encrypted.
        @print Output: The encrypted message.

    '''

    BLOCK_SIZE = 16  # 128 bit AES encryption(16 bytes)
    PADDING = '{'

    pad = lambda s: s+(BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))

    # secret = os.urandom(BLOCK_SIZE)
    # print 'encryption key:', secret
    # fileWrite('key.txt',secret)
    secret = open('key.txt','r').read()

    cipher = AES.new(secret)

    encoded = EncodeAES(cipher,privateInfo)

    fileWrite('message.txt', encoded)
    return encoded
    # print 'Encrypted string:', encoded
    # decrypt()
    


# f = raw_input("Enter message to be encoded: ")
# message = f
# encryption(message)


