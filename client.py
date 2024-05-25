import socket
import zlib
import io
from PIL import Image  # Requires installation of Pillow package

class RemoteDesktopClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = True

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print("Connected to server.")
            while self.running:
                self.handle_server_response()
        except Exception as e:
            print("Error connecting to server:", e)

    def handle_server_response(self):
        try:
            command = input("Enter command (screenshot/exit): ")
            self.client_socket.sendall(command.encode())
            if command.lower() == "exit":
                self.running = False
                return
            elif command.lower() == "screenshot":
                self.receive_screenshot()
        except Exception as e:
            print("Error handling server response:", e)

    def receive_screenshot(self):
        try:
            compressed_data = self.client_socket.recv(4096)  # Receive compressed screenshot data
            screenshot_data = zlib.decompress(compressed_data)  # Decompress the data
            image = Image.open(io.BytesIO(screenshot_data))  # Load image from bytes
            image.show()  # Display the screenshot
        except Exception as e:
            print("Error receiving screenshot:", e)

if __name__ == "__main__":
    client = RemoteDesktopClient('localhost', 9999)
    client.connect()
