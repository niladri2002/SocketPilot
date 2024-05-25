import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import socket
import os

class ClientGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Client")
        self.master.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        self.host_label = ttk.Label(self.master, text="Server IP:")
        self.host_label.grid(row=0, column=0, padx=10, pady=10)

        self.host_entry = ttk.Entry(self.master)
        self.host_entry.grid(row=0, column=1, padx=10, pady=10)

        self.port_label = ttk.Label(self.master, text="Server Port:")
        self.port_label.grid(row=1, column=0, padx=10, pady=10)

        self.port_entry = ttk.Entry(self.master)
        self.port_entry.grid(row=1, column=1, padx=10, pady=10)

        self.connect_button = ttk.Button(self.master, text="Connect", command=self.connect_to_server)
        self.connect_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.command_label = ttk.Label(self.master, text="Command:")
        self.command_label.grid(row=3, column=0, padx=10, pady=10)

        self.command_entry = ttk.Entry(self.master)
        self.command_entry.grid(row=3, column=1, padx=10, pady=10)

        self.send_button = ttk.Button(self.master, text="Send Command", command=self.send_command)
        self.send_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.output_text = tk.Text(self.master, wrap='word', height=10, width=40)
        self.output_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.scrollbar = ttk.Scrollbar(self.master, orient=tk.VERTICAL, command=self.output_text.yview)
        self.scrollbar.grid(row=5, column=2, sticky='ns')
        self.output_text.config(yscrollcommand=self.scrollbar.set)

    def connect_to_server(self):
        host = self.host_entry.get()
        port = int(self.port_entry.get())

        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((host, port))
            self.output_text.insert(tk.END, "[+] Connected to server\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to connect to server: {e}")

    def send_command(self):
        if hasattr(self, 'client_socket'):
            command = self.command_entry.get()
            try:
                self.client_socket.send(command.encode())
                response = self.client_socket.recv(1024).decode()
                self.output_text.insert(tk.END, f"Server response: {response}\n")

                if response.startswith("File contents:"):
                    filename = command.split()[1]
                    with open(filename, "wb") as file:
                        while True:
                            data = self.client_socket.recv(1024)
                            if not data:
                                break
                            file.write(data)
                    self.output_text.insert(tk.END, f"File '{filename}' downloaded successfully.\n")
                
                elif response.startswith("Server output: Changed directory to"):
                    directory = response.split()[-1]
                    self.output_text.insert(tk.END, f"Server output: Changed directory to {directory}\n")
                
                else:
                    pass  # Handle other responses here

            except Exception as e:
                self.output_text.insert(tk.END, f"Error: {e}\n")
        else:
            messagebox.showwarning("Warning", "Not connected to server")


def main():
    root = tk.Tk()
    app = ClientGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
