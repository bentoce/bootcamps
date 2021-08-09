import  socket
import  sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!!!")
        print("Erro: {}".format(e))

    sys.exit()
    print("Socker criado com sucesso")
    HostAlvo = input("Digite o Host ou Ip a ser conectado")
    PortaAlvo = input("Digite a porta a ser conectada:")


