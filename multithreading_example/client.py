import socket

def start_client():
    HOST = '127.0.0.1'
    PORT = 5050

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"time")
        data = s.recv(1024)
        print("Empfangene Antwort:", data.decode('utf-8'))

if __name__ == "__main__":
    start_client()
