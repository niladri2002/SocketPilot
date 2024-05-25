'''import socket

def main():
    host = "192.168.29.225"  # Server IP address
    port = 9999         # Server port

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print("[+] Connected to server")

        while True:
            command = input("Enter command ('exit' to quit): ")
            if command.lower() == "exit":
                break
            client_socket.send(command.encode())

            response = client_socket.recv(1024).decode()
            print("Server response:", response)

            if response == "OK":
                data = client_socket.recv(1024).decode()
                print("File contents:")
                print(data)

    except Exception as e:
        print("[-] Error:", e)

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
'''
import socket
import os

def main():
    host = "192.168.29.245"  # Server IP address
    port = 9999         # Server port

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print("[+] Connected to server")

        while True:
            command = input("Enter command ('exit' to quit): ")
            if command.lower() == "exit":
                break
            client_socket.send(command.encode())

            response = client_socket.recv(1024).decode()
            print("Server response:", response)

            if response.startswith("File contents:"):
                filename = command.split()[1]
                with open(filename, "wb") as file:
                    while True:
                        data = client_socket.recv(1024)
                        if not data:
                            break
                        file.write(data)
                print(f"File '{filename}' downloaded successfully.")
                
            else:
                print("Server did not send file data.")

    except Exception as e:
        print("[-] Error:", e)

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
