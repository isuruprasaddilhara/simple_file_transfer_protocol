import socket
import tqdm

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.8.188",888))
print("[+] Waiting for a connection... ")
s.listen(5)
def receive_file(client):
    file_name = client.recv(1024).decode()
    file_size = client.recv(1024).decode()
    
    progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000,total=int(file_size))
    
    with open("/home/isuru/Desktop/"+file_name,"wb") as file:
        c=0
        while c<=int(file_size):
            data = client.recv(1024)
            if not(data):
                break
            file.write(data)
            c+=len(data)
            progress.update(1024)

    if c == int(file_size):
        print("File Transfer Completed.")
    else:
        print("Error! File Transfer not completed.")

while True:
    client,addr = s.accept()
    print(f"We got a connection from {addr}")
    receive_file(client)
    client.close()

