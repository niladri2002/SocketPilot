import socket
import pyscreenshot as ImageGrab  
import matplotlib.pyplot as plt
import pygetwindow as gw
import pyscreenshot as ImageGrab

screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
screenshot.show()
class RemoteDesktopServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            print("Server listening on {}:{}".format(self.host, self.port))
            self.accept_connections()
        except Exception as e:
            print("Error starting server:", e)

    def accept_connections(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("Client connected:", client_address)
            self.clients.append((client_socket, client_address))
            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        try:
            while True:
                command = client_socket.recv(1024).decode().strip()  # Receive client's command
                if command == "screenshot":
                    self.send_screenshot(client_socket)
                elif command == "exit":
                    print("Client disconnected")
                    self.clients.remove((client_socket, client_address))
                    break
                else:
                    print("Invalid command from client:", command)
        except ConnectionResetError:
            print("Client disconnected unexpectedly")
            self.clients.remove((client_socket, client_address))

    def send_screenshot(self, client_socket):
        try:
            screenshot = ImageGrab.grab() 
            plt.imshow(screenshot)
            plt.show()
            screenshot_bytes = screenshot.tobytes()
            print(screenshot_bytes)   # Get the bytes of the screenshot
            client_socket.sendall(screenshot_bytes)  # Send the screenshot bytes to the client
        except Exception as e:
            print("Error sending screenshot:", e)

if __name__ == "__main__":
    server = RemoteDesktopServer('localhost', 9999)
    server.start()
