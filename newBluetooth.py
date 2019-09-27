# from bluetooth import *

# print("performing inquiry...")

# nearby_devices = discover_devices(lookup_names = True)

# print("found %d devices" % len(nearby_devices))

# for name, addr in nearby_devices:
#      print(" %s - %s" % (addr, name))


# from bluetooth import *

# server_socket=BluetoothSocket( RFCOMM )

# server_socket.bind(("", 3 ))
# server_socket.listen(1)

# client_socket, address = server_socket.accept()

# data = client_socket.recv(1024)

# print("received [%s]" % data)

# client_socket.close()
# server_socket.close()


import bluetooth

print(bluetooth)

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 0
server_sock.bind(("",port))
server_sock.listen(1)
print("listening on port %d" % port)

uuid = "1e0ca4ea-299d-4335-93eb-27fcfe7fa848"
bluetooth.advertise_service( server_sock, "FooBar Service", uuid )

client_sock,address = server_sock.accept()
print("Accepted connection from ",address)

data = client_sock.recv(1024)
print("received [%s]" % data)

client_sock.close()
server_sock.close()