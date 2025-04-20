import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
from ftp.ftp_sender import ftp_send_file
from ftp.ftp_receiver import ftp_receive_file
from telnet.telnet_server import start_telnet_server
from telnet.telnet_client import start_telnet_client

class NetworkApp:
	def __init__(self, root):
		self.root = root
		self.root.title("ProtoMUX - Network Tool")
		self.root.geometry("450x300")
		self.root.resizable(False, False)

		self.protocol = tk.StringVar(value="FTP")
		self.role = tk.StringVar(value="Sender")
		self.ip = tk.StringVar()
		self.port = tk.StringVar()
		self.file_path = tk.StringVar()

		self.setup_widgets()

	def setup_widgets(self):
		padding = {'padx': 10, 'pady': 10}

		ttk.Label(self.root, text="Select Protocol:").grid(column=0, row=0, sticky="w", **padding)
		ttk.Combobox(self.root, textvariable=self.protocol, values=["FTP", "Telnet"], state="readonly").grid(column=1, row=0, **padding)

		ttk.Label(self.root, text="Select Role:").grid(column=0, row=1, sticky="w", **padding)
		ttk.Combobox(self.root, textvariable=self.role, values=["Sender", "Receiver"], state="readonly").grid(column=1, row=1, **padding)

		ttk.Label(self.root, text="Target IP Address:").grid(column=0, row=2, sticky="w", **padding)
		ttk.Entry(self.root, textvariable=self.ip).grid(column=1, row=2, **padding)

		ttk.Label(self.root, text="Port:").grid(column=0, row=3, sticky="w", **padding)
		ttk.Entry(self.root, textvariable=self.port).grid(column=1, row=3, **padding)

		self.file_btn = ttk.Button(self.root, text="Select File", command=self.browse_file)
		self.file_btn.grid(column=0, row=4, columnspan=2, **padding)

		ttk.Button(self.root, text="Start", command=self.start_action).grid(column=0, row=5, columnspan=2, **padding)

	def browse_file(self):
		path = filedialog.askopenfilename()
		if path:
			self.file_path.set(path)

	def start_action(self):
		protocol = self.protocol.get()
		role = self.role.get()
		ip = self.ip.get()
		port = int(self.port.get())
		file_path = self.file_path.get()

		if protocol == "FTP":
			if role == "Sender":
				if not file_path or not ip:
					messagebox.showerror("Error", "Please select a file and enter IP")
					return
				threading.Thread(target=ftp_send_file, args=(ip, file_path, port)).start()
			else:
				threading.Thread(target=ftp_receive_file, args=(ip, port)).start()

		elif protocol == "Telnet":
			if role == "Sender":
				start_telnet_client(ip, port)
			else:
				threading.Thread(target=start_telnet_server, args=(ip, port)).start()

if __name__ == "__main__":
	root = tk.Tk()
	app = NetworkApp(root)
	root.mainloop()
