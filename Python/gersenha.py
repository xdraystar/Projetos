import tkinter as tk
from tkinter import ttk
import random
import string

def gera_password():
    password_length = int(length_combobox.get())
    include_special_chars = special_chars_var.get()

    characters = string.ascii_letters + string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_display.config(text="Password: " + password)

# Criação da janela principal
root = tk.Tk()
root.title("Gerador de Passwords")

# Configuração do comprimento da password usando Combobox
length_label = tk.Label(root, text="Selecione o comprimento:")
length_label.pack()

length_values = [str(i) for i in range(8, 21)]  # Comprimentos de password de 8 a 20 caracteres
length_combobox = ttk.Combobox(root, values=length_values)
length_combobox.set("8")  # Valor padrão
length_combobox.pack()

# Checkbox para caracteres especiais
special_chars_var = tk.BooleanVar()
special_chars_checkbox = ttk.Checkbutton(root, text="Incluir caracteres especiais", variable=special_chars_var)
special_chars_checkbox.pack()

# Botão para gerar password
generate_button = tk.Button(root, text="Criar Password", command=gera_password)
generate_button.pack()

# Exibição da password gerada
password_display = tk.Label(root, text="Password: ")
password_display.pack()

# Iniciar a interface gráfica
root.mainloop()
