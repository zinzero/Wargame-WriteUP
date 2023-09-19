import random
import string

from pwn import *


#while True:

rchr = string.ascii_uppercase + string.ascii_lowercase + string.digits
lst = list(set(rchr))

for i in lst:
    errormsg = "There's been an error"
    
    r = remote("chal.pctf.competitivecyber.club", 4757)

#    rchr = string.ascii_letters + string.digits + "_"
   # flag = ''.join(random.choice(rchr) for _ in range(13))

#    print(flag)
   # r.sendline("pctf{"+flag+"}")
    r.sendline("pctf{Tim3ingI8N3a" + i + "}")

    response = r.recvall()
    response = response.decode('utf-8')

    length = len(response)

    print(length)
    if length != 591:
        print(response)
        break


    if errormsg not in response:
        break
r.close()

