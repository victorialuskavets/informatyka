# load additional Python module
import socket, sys


# create TCP/IP socket
sock = socket.socket()

port = 25002
print ('starting up on port ', port)
sock.bind(('localhost', port))

sock.listen(1)

while True:
    # wait for a connection
    print ('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        # show who connected to us
        print ('connection from', client_address)

        # receive the data in small chunks and print it
        while True:
            data = connection.recv(512).decode()
            if data:
                # output received data
                print ("Data: ", data)
            else:
                # no more data -- quit the loop
                print ("no more data.")
                break

    finally:
        # Clean up the connection
        connection.close()

sock.close()