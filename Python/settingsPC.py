
import tkinter as tk
import platform
import socket


# função para ver endereço IP do PC
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    ip_label.config(text=f"Endereço IP: {ip_address}")

# função para ver o sistema do PC
def show_system_info():
    sistema = platform.system()
    versao = platform.version()
    machine = platform.machine()
    processor = platform.processor()

    system_info = f"Sistema: {sistema}\n" \
                 f"Versão completa: {versao}\n" \
                 f"Máquina: {machine}\n" \
                 f"Processador: {processor}"

    system_info_label.config(text=system_info)





# Cria a Janela 
root = tk.Tk()
root.title("Informações do Sistema")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Mostra informação do sistema PC
system_info_label = tk.Label(frame, text="", wraplength=300)
system_info_label.pack()

show_system_button = tk.Button(frame, text="Mostrar informações do sistema", command=show_system_info)
show_system_button.pack(pady=10)
#--------------------------------------------


# Mostra informação do endereço IP do PC
ip_label = tk.Label(frame, text="")
ip_label.pack()

get_ip_button = tk.Button(frame, text="Verificar endereço IP", command=get_ip_address)
get_ip_button.pack(pady=10)
#--------------------------------------------




root.mainloop()