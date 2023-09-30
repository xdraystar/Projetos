import tkinter as tk
from tkinter import messagebox

def check_winner(player):
    for i in range(3):
        if (buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] == player) or \
           (buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] == player):
            return True

    if (buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == player) or \
       (buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] == player):
        return True

    return False

def is_full():
    return all(button["text"] != "" for row in buttons for button in row)

def on_button_click(row, col):
    if buttons[row][col]["text"] == "" and not check_winner("X") and not check_winner("O"):
        buttons[row][col]["text"] = current_player
        buttons[row][col]["state"] = "disabled"
        
        if check_winner(current_player):
            display_result(f"{current_player} venceu!")
        elif is_full():
            display_result("Empate!")
        else:
            switch_player()

def display_result(result):
    label.config(text=result)
    for row in buttons:
        for button in row:
            button.config(state="disabled")

def reset_game():
    global current_player
    current_player = "X"
    label.config(text="Jogador Atual: X")
    
    for row in buttons:
        for button in row:
            button.config(text="", state="normal")

def exit_game():
    if messagebox.askyesno("Sair do Jogo", "Deseja sair do jogo?"):
        root.destroy()

def switch_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Jogador Atual: {current_player}")

# Criação da janela principal
root = tk.Tk()
root.title("Jogo da Velha")

# Variáveis globais
current_player = "X"

# Criação dos botões
buttons = [[None, None, None], [None, None, None], [None, None, None]]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=("Helvetica", 24), width=5, height=2,
                                      command=lambda row=row, col=col: on_button_click(row, col))
        buttons[row][col].grid(row=row, column=col)

# Label para mostrar o jogador atual
label = tk.Label(root, text="Jogador Atual: X", font=("Helvetica", 14))
label.grid(row=3, columnspan=3)

# Botões de reset e saída
reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.grid(row=4, column=0, columnspan=2)

exit_button = tk.Button(root, text="Sair", command=exit_game)
exit_button.grid(row=4, column=2, columnspan=1)

root.mainloop()
