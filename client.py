import socket
import os 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",888))

def send_file():
    file_name = input("Enter File Name : ")
    file_size = os.path.getsize(file_name)
    s.send(file_name.encode())
    s.send(str(file_size).encode())

    with open(file_name,"rb") as file:
        c=0
        while c<=file_size:
            data=file.read(1024)
            if not(data):
                break
            s.sendall(data)
            c+=len(data)

    print("File Transfer completed.")

send_file()