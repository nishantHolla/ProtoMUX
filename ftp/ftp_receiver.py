import socket
import os

def ftp_receive_file(bind_ip='0.0.0.0', port=2121):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((bind_ip, port))
	sock.listen(1)
	print(f"[*] Listening on {bind_ip}:{port} for incoming files...")

	conn, addr = sock.accept()
	print(f"[+] Connection from {addr[0]}:{addr[1]}")

	# Receive filename length and filename
	filename_len = int.from_bytes(conn.recv(2), 'big')
	filename = conn.recv(filename_len).decode()

	script_dir = os.path.dirname(os.path.abspath(__file__))
	save_path = os.path.join(script_dir, filename)

	with open(save_path, 'wb') as f:
		print(f"[+] Receiving file: {filename}")
		while True:
			data = conn.recv(4096)
			if not data:
				break
			f.write(data)

	print(f"[+] File '{filename}' received successfully.")
	conn.close()

if __name__ == "__main__":
	ftp_receive_file()
