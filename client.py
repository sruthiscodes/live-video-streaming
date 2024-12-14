import socket
import cv2
import pickle
import struct
import imutils
import ssl

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = "192.168.0.100"
port = 5006

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

ssl_client_socket = context.wrap_socket(client_socket, server_hostname=host_ip)
ssl_client_socket.connect((host_ip, port))

data = b""
payload_size = struct.calcsize("Q")
while True:
    while len(data) < payload_size:
        packet = ssl_client_socket.recv(4 * 1024)
        if not packet:
            break
        data += packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]
    while len(data) < msg_size:
        data += ssl_client_socket.recv(4 * 1024)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame = pickle.loads(frame_data)
    cv2.imshow("Receiving...", frame)
    key = cv2.waitKey(10)
    if key == 13:
        break

ssl_client_socket.close()
