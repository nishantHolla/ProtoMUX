import socket
import os

def ftp_send_file(dest_ip, file_path, port=2121):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((dest_ip, port))

	filename = os.path.basename(file_path)
	filename_encoded = filename.encode()
	sock.send(len(filename_encoded).to_bytes(2, 'big'))
	sock.send(filename_encoded)

	with open(file_path, 'rb') as f:
		print(f"[*] Sending file: {filename}")
		while chunk := f.read(4096):
			sock.send(chunk)

	print(f"[+] File '{filename}' sent successfully.")
	sock.close()

if __name__ == "__main__":
	ftp_send_file('127.0.0.1', '')
