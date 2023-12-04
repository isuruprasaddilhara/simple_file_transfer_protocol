import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost",888))
print("[+] Waiting for a connection... ")
s.listen(5)

def receive_file(client):
    file_name = client.recv(1024).decode()
    file_size = client.recv(1024).decode()

    with open("D:\Education Related\\"+file_name,"wb") as file:
        c=0
        while c<=int(file_size):
            data = client.recv(1024)
            if not(data):
                break
            file.write(data)
            c+=len(data)
    print("Completed.")

while True:
    client,addr = s.accept()
    print(f"We got a connection from {addr}")
    receive_file(client)
    client.close()

