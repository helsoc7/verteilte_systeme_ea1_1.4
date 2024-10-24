import socket
from datetime import datetime

# Server IP und Port festlegen
HOST = '127.0.0.1'
PORT = 5050

# Server-Socket erstellen (IPv4, TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Socket an die IP und den Port binden
    s.bind((HOST, PORT)) 
    # Auf eingehende Verbindungen warten
    s.listen() 
    print(f"Server läuft und wartet auf Verbindungen auf {HOST}:{PORT}")
    
    # Verbindung akzeptieren
    conn, addr = s.accept()
    with conn:
        print(f"Verbindung zu {addr} hergestellt")
        while True:
            # Daten vom Client empfangen
            data = conn.recv(1024)  
            if not data:
                break
            if data.decode('utf-8') == "time":
                # Aktuelles Datum und Uhrzeit ermitteln
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # Zeit zurücksenden
                conn.sendall(current_time.encode('utf-8'))  
            else:
                conn.sendall(b"Unbekannte Anfrage")
    conn.close()
