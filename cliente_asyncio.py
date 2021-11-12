import sys
import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = sys.argv[1]
PUERTO = int(sys.argv[2])
HEADER=1024
HEADER2=2048
path = cliente.recv(HEADER)
cliente.connect((HOST, PUERTO))
def main():
    while True:
        print("Nueva conexion")
        comando = input(f"Digite comando{path.decode()}: ")
        if comando.lower() == "exit":
            cliente.close()
            break
        cliente.send(comando.encode())
        output = cliente.recv(HEADER2).decode()
        print(output)
        
if __name__=='__main__':
    main()