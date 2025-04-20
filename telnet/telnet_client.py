import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import socket
import re

def strip_ansi_escape(text):
	text = re.sub(r'\x1B\[[0-?]*[ -/]*[@-~]', '', text)
	text = re.sub(r'\x1B\].*?\x07', '', text)
	return text

def start_telnet_client(host, port):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((host, port))

	client_window = tk.Toplevel()
	client_window.title(f"Telnet Client - Connected to {host}:{port}")
	client_window.geometry("700x500")

	client_window.rowconfigure(0, weight=1)
	client_window.columnconfigure(0, weight=1)
	client_window.resizable(False, False)

	output_text = scrolledtext.ScrolledText(client_window, wrap=tk.WORD, state="disabled", font=("Courier", 10))
	output_text.grid(row=0, column=0, sticky="nsew")

	input_entry = tk.Entry(client_window, font=("Courier", 10))
	input_entry.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
	client_window.columnconfigure(0, weight=1)

	def send_command(event=None):
		cmd = input_entry.get() + "\n"
		if cmd.strip():
			client.sendall(cmd.encode())
		input_entry.delete(0, tk.END)

	def receive_output():
		while True:
			try:
				data = client.recv(4096)
				if not data:
					break
				clean = strip_ansi_escape(data.decode(errors="ignore"))
				output_text.configure(state="normal")
				output_text.insert(tk.END, clean)
				output_text.see(tk.END)
				output_text.configure(state="disabled")
			except OSError:
				break

	input_entry.bind("<Return>", send_command)
	threading.Thread(target=receive_output, daemon=True).start()

	client_window.mainloop()
