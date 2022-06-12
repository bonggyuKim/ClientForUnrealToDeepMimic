import socket

HOST = "192.168.0.43"
PORT = 3000
data_size = 8000

agentNum = 0


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    print("Socket Ready")
    client, address = server.recvfrom(3001)

    data = client.decode()
    print(data)
    action = "bytes('hi', 'utf-8')"
    server.sendto(action.encode(), address)
    print("hi")

if __name__ == '__main__':
    main()
