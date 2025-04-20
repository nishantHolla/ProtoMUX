from telnet.telnet_server import start_telnet_server
from ftp.ftp_receiver import ftp_receive_file
from ftp.ftp_sender import ftp_send_file

if __name__ == "__main__":
	print("Select protocol")
	while True:
		protocol_select = int(input("1. FTP\n2.Telnet\n"))
		if protocol_select > 0 and protocol_select < 3:
			break

	if protocol_select == 1:
		print("Select role")
		while True:
			role_select = int(input("1. Sender\n2. Receiver\n"))
			if role_select > 0 and role_select < 3:
				break

		if role_select == 1:
			ip = input("Enter destination ip")
			file = input("Enter file path")
			ftp_send_file(ip, file)
		else:
			ftp_receive_file()

	else:
		start_telnet_server()
