#by maksp

from operator import contains
import pwn

conn = pwn.remote('surctf.ru', 5000)
conn.recvlines(2)

while True:
    recv = conn.recvline().decode('utf-8')
    print("RANGE STRING: ", recv)
    
    if contains(recv, 'won'):
        recv = conn.recvline().decode('utf-8')
        print("FLAG: ", recv)
        exit()

    splited = recv.split()

    left = int(splited[-2][1:-1])
    right = int(splited[-1][:-1])
    print(f"Left: {left}, right {right}")

    conn.recvline()
    while True:
        current = (left+right)//2
        conn.sendline(str(current).encode('utf-8'))
        print("SENT TO SERVER: ", str(current))

        recv = conn.recvline().decode('utf-8')
        print("GOT FROM SERVER: ", recv)

        if contains(recv, 'small'):
            left = current + 1
        elif contains(recv, 'much'):
            right = current - 1
        else:
            break

#by maksp