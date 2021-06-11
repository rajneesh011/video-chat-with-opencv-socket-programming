import socket
import cv2
import pickle
import struct


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

print("\t\t\t\n************************************************")
print('HOST IP:', host_ip)
print("\t\t\t\n************************************************")

port = 2345
socket_address = ('client-ip here', port)


print("\t\t\t\n************************************************")
print("Socket Created")
print("\t\t\t\n************************************************")

server_socket.bind(socket_address)


print("\t\t\t\n************************************************")
print("Socket Bind Successfully")
print("\t\t\t\n************************************************")


server_socket.listen(5)
print("\t\t\t\n************************************************")
print("LISTENING AT:", socket_address)
print("\t\t\t\n************************************************")

print("\t\t\t\n************************************************")
print("Socket Accept")
print("\t\t\t\n************************************************")
while True:
    client_socket, addr = server_socket.accept()
    print('GOT CONNECTION FROM:', addr)
    if client_socket:
        vid = cv2.VideoCapture(0)

        while(vid.isOpened()):
            img, frame = vid.read(vid)
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a))+a
            client_socket.sendall(message)

            cv2.imshow('TRANSMITTING VIDEO', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()
print("\t\t\t\n************************************************")
print("Thank you for connecting ")
print("\t\t\t\n************************************************")
