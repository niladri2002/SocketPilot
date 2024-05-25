# import socket
# import os

# def send_file(conn, filename):
#     try:
#         with open(filename, "rb") as file:
#             data = file.read()
#             conn.sendall(data)
#         return True
#     except Exception as e:
#         conn.sendall(str(e).encode())
#         return False

# def list_files():
#     try:
#         files = os.listdir()
#         return "\n".join(files)
#     except Exception as e:
#         return str(e)

# def move_directory(directory):
#     try:
#         os.chdir(directory)
#         return f"Moved to directory: {os.getcwd()}"
#     except Exception as e:
#         return str(e)

# def handle_client(conn, addr):
#     print(f"[+] Accepted connection from {addr[0]}:{addr[1]}")
#     current_directory = os.getcwd()

#     while True:
#         try:
#             data = conn.recv(1024).decode().strip()
#             if not data:
#                 print(f"[*] Connection closed by {addr[0]}:{addr[1]}")
#                 break
#             elif data.lower() == "exit":
#                 print(f"[*] Closing connection with {addr[0]}:{addr[1]}")
#                 conn.close()
#                 break
#             elif data.lower() == "ls":
#                 file_list = list_files()
#                 conn.sendall(file_list.encode())
#             elif data.lower().startswith("cd"):
#                 directory = data[3:].strip()
#                 response = move_directory(directory)
#                 conn.sendall(response.encode())
#             elif data.lower().startswith("get"):
#                 filename = data[4:].strip()
#                 if os.path.exists(filename):
#                     conn.sendall("OK".encode())
#                     send_file(conn, filename)
#                 else:
#                     conn.sendall("File not found".encode())
#             else:
#                 conn.sendall("Invalid command".encode())
#         except Exception as e:
#             print(f"[*] Error with {addr[0]}:{addr[1]} - {e}")
#             break

# def main():
#     host = "192.168.29.225"  # Listen on all available interfaces
#     port = 9999

#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind((host, port))
#     server_socket.listen(5)

#     print(f"[*] Listening on {host}:{port}")

#     while True:
#         conn, addr = server_socket.accept()
#         handle_client(conn, addr)

# if __name__ == "__main__":
#     main()



# import socket
# import os

# def send_file(conn, filename):
#     try:
#         with open(filename, "rb") as file:
#             data = file.read()
#             conn.sendall(data)
#         return True
#     except Exception as e:
#         conn.sendall(str(e).encode())
#         return False

'''import socket

import os
import matplotlib.pyplot as plt

from PIL import Image
import io

def send_file(conn, filename):
    try:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            try:
                with open(filename, "rb") as file:
                    img_data = file.read()
                    print(f"[*] Image file '{filename}' size:", len(img_data))
                    conn.sendall(img_data)
                    print(f"[*] Image file '{filename}' sent successfully.")
                return True
            except Exception as e:
                conn.sendall(str(e).encode())
                return False
        else:
            with open(filename, "rb") as file:
                while True:
                    data = file.read(1024)
                    if not data:
                        break
                    conn.sendall(data)
                print(f"[*] File '{filename}' sent successfully.")
        return True
    except Exception as e:
        conn.sendall(str(e).encode())
        return False


# Other functions remain unchanged...


def list_files():
    try:
        files = os.listdir()
        return "\n".join(files)
    except Exception as e:
        return str(e)

def move_directory(directory):
    try:
        os.chdir(directory)
        return f"Moved to directory: {os.getcwd()}"
    except Exception as e:
        return str(e)

def handle_client(conn, addr):
    print(f"[+] Accepted connection from {addr[0]}:{addr[1]}")
    current_directory = os.getcwd()

    while True:
        try:
            data = conn.recv(1024).decode().strip()
            if not data:
                print(f"[*] Connection closed by {addr[0]}:{addr[1]}")
                break
            elif data.lower() == "exit":
                print(f"[*] Closing connection with {addr[0]}:{addr[1]}")
                conn.close()
                break
            elif data.lower() == "ls":
                file_list = list_files()
                conn.sendall(file_list.encode())
            elif data.lower().startswith("cd"):
                directory = data[3:].strip()
                response = move_directory(directory)
                conn.sendall(response.encode())
            elif data.lower().startswith("get"):
                filename = data[4:].strip()
                if os.path.exists(filename):
                    conn.sendall("OK".encode())
                    send_file(conn, filename)
                else:
                    conn.sendall("File not found".encode())
            elif data.lower().startswith("open"):
                filename = data[5:].strip()
                if os.path.exists(filename):
                    conn.sendall("OK".encode())
                    send_file(conn, filename)
                else:
                    conn.sendall("File not found".encode())
            else:
                conn.sendall("Invalid command".encode())
        except Exception as e:
            print(f"[*] Error with {addr[0]}:{addr[1]} - {e}")
            break

def main():
    host = "192.168.29.225"  # Listen on all available interfaces
    port = 9999

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"[*] Listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        handle_client(conn, addr)

if __name__ == "__main__":
    main()
'''
import socket
import os

def send_file(conn, filename):
    try:
        with open(filename, "rb") as file:
            file_data = file.read()
            conn.sendall(file_data)
            print(f"[*] File '{filename}' sent successfully.")
        return True
    except Exception as e:
        conn.sendall(str(e).encode())
        return False

def list_files(directory="."):
    try:
        files = os.listdir(directory)
        return "\n".join(files)
    except Exception as e:
        return str(e)

def handle_client(conn, addr):
    print(f"[+] Accepted connection from {addr[0]}:{addr[1]}")

    while True:
        try:
            data = conn.recv(1024).decode().strip()
            if not data:
                print(f"[*] Connection closed by {addr[0]}:{addr[1]}")
                break
            elif data.lower() == "exit":
                print(f"[*] Closing connection with {addr[0]}:{addr[1]}")
                conn.close()
                break
            elif data.lower() == "ls":
                file_list = list_files()
                conn.sendall(file_list.encode())
            elif data.lower().startswith("cd "):
                directory = data[3:].strip()
                if directory == "..":
                    os.chdir("..")
                else:
                    os.chdir(directory)
                file_list = list_files()
                conn.sendall(file_list.encode())
            elif data.lower().startswith("get "):
                filename = data[4:].strip()
                send_file(conn, filename)
            else:
                send_file(conn, data)
        except Exception as e:
            print(f"[*] Error with {addr[0]}:{addr[1]} - {e}")
            break

def main():
    host = "192.168.29.225" 
    port = 9999        

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"[*] Listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        handle_client(conn, addr)

    server_socket.close()

if __name__ == "__main__":
    main()
