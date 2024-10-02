import sys, os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad



data = ''
key = 'LR9Jb7PMkAEef7z3'

def encrypt(raw):
        raw = pad(raw.encode(),16)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt(raw))

def decrypt(enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        return unpad(cipher.decrypt(enc),16)


if len(sys.argv) > 2:
    oper = sys.argv[1]
    data = sys.argv[2]
    if os.environ.get('CYBERKEY'):
        key = os.environ.get('CYBERKEY')
    else:
        print('Not found ENV(CYBERKEY)')
    if oper == 'enc':
        encrypted = encrypt(data)
        print('encrypted ECB Base64:',encrypted.decode("utf-8", "ignore"))
    elif oper == 'dec':
        decrypted = decrypt(data)
        #print('data: ',decrypted.decode("utf-8", "ignore"))
        print('Decrypted data...')
    else:
        print(f'Operation /{oper}/ Not found')
else:
     print('Not found argumets')