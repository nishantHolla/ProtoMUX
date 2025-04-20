import socket
import os
import pty
import select

def handle_client(client_sock):
	pid, fd = pty.fork()
	if pid == 0:
		os.execvp("bash", ["bash"])
	else:
		try:
			client_sock.setblocking(False)
			while True:
				rlist, _, _ = select.select([client_sock, fd], [], [])
				if client_sock in rlist:
					data = client_sock.recv(1024)
					if not data:
						break
					os.write(fd, data)
				if fd in rlist:
					try:
						data = os.read(fd, 1024)
						if not data:
							break
						client_sock.sendall(data)
					except OSError:
						break
		finally:
			os.close(fd)
			client_sock.close()

def start_telnet_server(ip, port):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((ip, port))
		s.listen()

		print(f"Telnet PTY shell server running on {ip}:{port}")
		while True:
			client_sock, addr = s.accept()
			print(f"[+] Connection from {addr}")
			pid = os.fork()
			if pid == 0:
				s.close()
				handle_client(client_sock)
				os._exit(0)
			else:
				client_sock.close()

if __name__ == "__main__":
	start_telnet_server()

