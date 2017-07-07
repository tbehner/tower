import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('tower.chall.polictf.it', 31337))
with open('tower.txt', 'w') as tf:
    try:
        while True:
            resp = s.recv(1024 * 1024)
            if resp != '':
                tf.write(resp.decode('utf-8'))
    except KeyboardInterrupt:
        sys.exit(0)

