import socket

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(('MAC-Address', 4))

try:
    while True:
        message = input("")
        client.send(message.encode())
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")

except OSError as e:
    pass

client.close()