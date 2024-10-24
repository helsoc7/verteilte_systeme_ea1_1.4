import socket
import threading
from datetime import datetime

# Server-Funktion
def start_server():
    HOST = '127.0.0.1'
    PORT = 5050

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server läuft und wartet auf Verbindungen auf {HOST}:{PORT}")

        conn, addr = s.accept()
        with conn:
            print(f"Verbindung zu {addr} hergestellt")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                if data.decode('utf-8') == "time":
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    conn.sendall(current_time.encode('utf-8'))
                else:
                    conn.sendall(b"Unbekannte Anfrage")

# Client-Funktion
def start_client():
    HOST = '127.0.0.1'
    PORT = 5050

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"time")
        data = s.recv(1024)
        print("Empfangene Antwort:", data.decode('utf-8'))

# Hauptfunktion, die sowohl Server als auch Client startet
def main():
    # Erstellen von zwei Threads: einen für den Server und einen für den Client
    server_thread = threading.Thread(target=start_server)
    client_thread = threading.Thread(target=start_client)

    # Server-Thread starten
    server_thread.start()

    # Warten, bis der Server bereit ist (kurze Verzögerung, damit der Server gestartet wird, bevor der Client eine Verbindung herstellt)
    threading.Event().wait(1)

    # Client-Thread starten
    client_thread.start()

    # Warten, bis beide Threads beendet sind
    server_thread.join()
    client_thread.join()

if __name__ == "__main__":
    main()
