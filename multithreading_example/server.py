import socket
import threading
from datetime import datetime

# Funktion, um eine einzelne Client-Anfrage zu bearbeiten
def handle_client(conn, addr):
    print(f"Verbindung zu {addr} hergestellt")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            if data.decode('utf-8') == "time":
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                conn.sendall(current_time.encode('utf-8'))
            else:
                conn.sendall(b"Unbekannte Anfrage")
    print(f"Verbindung zu {addr} geschlossen")

# Funktion, um den Server zu starten
def start_server():
    HOST = '127.0.0.1'
    PORT = 5050

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server läuft und wartet auf Verbindungen auf {HOST}:{PORT}")

        # Endlosschleife, um kontinuierlich Verbindungen zu akzeptieren
        while True:
            conn, addr = s.accept()  # Neue Verbindung akzeptieren
            # Jede neue Verbindung in einem separaten Thread verarbeiten
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()  # Startet die Bearbeitung des Clients in einem neuen Thread

# Hauptfunktion, die den Server startet
if __name__ == "__main__":
    start_server()
