import tkinter as tk
import datetime
# Cria janela
janela = tk.Tk()
janela.title("Data e Hora")

# Cria frame para atualizar data e ora
frame = tk.Frame(janela)
frame.pack()

# Criar label da data.
data_label = tk.Label(frame, text="Data:")
data_label.grid(column=0, row=0, padx=10, pady=10)

# Criar label da hora.
hora_label = tk.Label(frame, text="Hora:")
hora_label.grid()

# Criar função para atualizar label de data e hora
def atualizar():
  # Obtem data e hora atuais
  now = datetime.datetime.now()

  # Atualiza label da data
  data_label.config(text="Data: {}".format(now.strftime("%Y-%m-%d")))

  # Atualiza label da hora
  hora_label.config(text="Hora: {}".format(now.strftime("%H:%M:%S")))

# Chama a função atualizar a cada segundo
janela.after(1000, atualizar)

# Cria um botao para sair
botao_sair = tk.Button(janela, text="Sair", command=exit)
botao_sair.pack(side=tk.BOTTOM)

# Altera tamanho da janela em largura(200) e altura(100)
janela.geometry("250x100")

# Inicia o loop principal
janela.mainloop()