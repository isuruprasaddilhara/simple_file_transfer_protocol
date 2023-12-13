import server,client

def choose():
    print("1.Send a File ")
    print("2.Receive a File ")
    print("3.Exit")

    choise = int(input("What do you want to do :"))
    return choise

while True:
    choise = choose()
    if choise == 1:
        client.send()
    elif choise == 2:
        server.receive()
    elif choise == 3:
        break
    else:
        print("Invalid choise!!!")

print('')
print('----------------------------------------------------------------------------')