import socket
import os 
import tqdm

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.8.188",888))

def send_file():
    file_name = input("Enter File Name : ")
    file_size = os.path.getsize(file_name)
    s.send(file_name.encode())
    s.send(str(file_size).encode())

    progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000,total=int(file_size))

    with open(file_name,"rb") as file:
        c=0
        while c<=file_size:
            data=file.read(1024)
            if not(data):
                break
            s.sendall(data)
            c+=len(data)
            progress.update(1024)

    if c==file_size:
        print("\nFile Transfer completed.")
    else:
        print("Error! File Transfer not completed.")

send_file()