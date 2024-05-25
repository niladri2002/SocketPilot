import socket

host="127.0.0.1"
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(2)
    print("Server is listening for incoming connections...")
    
    conn, addr = server.accept()
    print("Connected to:", addr)

    while True:
        rcv = conn.recv(2048).decode()
        if not rcv:
            print("Client disconnected")
            break
        print("Received:", rcv)

except socket.error as e:
    print("Socket error:", e)

finally:
    server.close()
