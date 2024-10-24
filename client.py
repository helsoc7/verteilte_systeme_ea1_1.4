import socket

# Server IP und Port festlegen
HOST = '127.0.0.1'
PORT = 5050

# Client-Socket erstellen (IPv4, TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Verbindung zum Server aufbauen
    s.sendall(b"time")  # Anfrage an den Server senden
    
    # Antwort vom Server empfangen
    data = s.recv(1024)
    print("Empfangene Antwort:", data.decode('utf-8'))
    s.close()
