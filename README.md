# ProtoMUX

Telnet and FTP implementation in Python. A Computer Networks project demonstrating inter-device communication using socket programming.


## Team Members

- **Nishant Holla** - PES1UG23CS401  
  [GitHub](https://github.com/nishantHolla)
- **Pranav Hemanth** - PES1UG23CS433  
  [GitHub](https://github.com/Pranavh-2004)


## Features

- **FTP Mode**  
  Send and receive files between two devices on the same network.

- **Telnet Mode**  
  Remote PTY shell access via sockets, emulating a basic Telnet session.

- **Clean Tkinter GUI**  
  Select protocol, role, IP address, and file (if applicable) — all in a user-friendly interface.

## How to Run

1. Ensure both devices are connected to the same local network.
2. Clone this repository on both devices.

```bash
git clone https://github.com/your-repo/protomux.git
cd protomux
```

3. Run the GUI interface:

```bash
python main_gui.py
```

4. Select:

   - Protocol: **FTP** or **Telnet**
   - Role: **Sender** or **Receiver**
   - Enter the IP of the _other_ device
   - For FTP senders, choose a file to send

5. Click **Start** to begin the session!

---

## 📜 License

This project is built as part of the PES University Computer Networks Lab coursework. For educational use only.
