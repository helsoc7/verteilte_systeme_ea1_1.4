# Aufgabe 1.4 Client/Server
Betrachten Sie das Python-Programm zur Client/Server-Kommunikation im Buch in Fig 2.3
(Seite 59, Distributed Systems, Third edition, Version 3.03 (2020)).
Entwickeln Sie daraus ein Client/Server-Programm in Python über TCP, bei dem der Client
durch "send time" nach dem Datum und der Uhrzeit fragt, der Server dies beantwortet,
und der Client die Antwort zur Kontrolle ausgibt. Bringen Sie Ihr Programm auf Ihrem
Computer zum Laufen!
Hinweis: Server- und Client-Prozess können auf demselben Computer laufen, die für diesen
Testzweck über die IP-Nummer 127.0.0.1 (localhost) kommunizieren dürfen. Wählen Sie
selbst feste Portnummern.
Python ist eine Programmiersprache, die immer mehr Bedeutung gewinnt und in der jeder
Informatiker Erfahrungen gesammelt haben sollte. Diskutieren Sie gerne Ihre Lösungen in
der Newsgruppe.
---
## How to run
1. Run the server
```bash
python server.py
```
2. Run the client
```bash
python client.py
```
3. Der Client sendet "send time" an den Server und der Server antwortet mit dem aktuellen Datum und der Uhrzeit.
4. Der Client gibt die Antwort zur Kontrolle aus.
5. Der Client und der Server können auf demselben Computer laufen, die für diesen Testzweck über die IP-Nummer 127.0.0.1 (localhost) kommunizieren dürfen.

---
## Idee: Erweiterung des Programms um Threads für gleichzeitiges Ausführen von Server und Client
Wir schreiben eine main-Methode, die zwei Threads erstellt, einen für den Server und einen für den Client. Der Server und der Client können dann gleichzeitig ausgeführt werden.

## Endlosschleife für den Server (siehe Ordner multithreading_example)
Der Server wird in einer Endlosschleife ausgeführt, um mehrere Anfragen von Clients zu bearbeiten.
```python
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
    PORT = 5000

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

```
- Der Server läuft in einer Endlosschleife und wartet ununterbrochen auf neue Verbindungen (s.accept()).
- Sobald eine neue Verbindung akzeptiert wird, wird sie an die Funktion handle_client weitergeleitet.

### Multithreading für Client
Für jede neue Verbindung wird ein neuer Thread erstellt, um die Anfrage zu verarbeiten. Dadurch kann der Server mehrere Clients gleichzeitig bedienen, während er weiterhin auf neue Verbindungen wartet. Dafür haben wir die Funktion `handle_client` in einem separaten Thread gestartet.
Die Client-Funktion bleibt gleich
```python
import socket

def start_client():
    HOST = '127.0.0.1'
    PORT = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"time")
        data = s.recv(1024)
        print("Empfangene Antwort:", data.decode('utf-8'))

if __name__ == "__main__":
    start_client()
```
