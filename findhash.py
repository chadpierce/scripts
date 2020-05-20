# find md5 hash where first chars equal digit - used for a ctf challenge

import hashlib

target = '0'
n = 0
#word = "R34llyG00dP455sW0rd"
while True:
    plaintext = str(n)
    #plaintext = str(word) + str(n)
    hash = hashlib.md5(plaintext.encode('ascii')).hexdigest()
    #if hash[2:].isdigit():
    if hash[:1] == target and hash.isdigit():
        #print(hash[:2] + '   ' + hash[30:])
        print('plaintext:"' + plaintext + '", md5:' + hash)
        #break
    n = n + 1
