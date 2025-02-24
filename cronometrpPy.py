import tkinter as tk
from tkinter import messagebox

# Função para atualizar o cronômetro
def update_timer():
    global remaining_time, is_running
    if is_running and remaining_time > 0:
        # Converte o tempo restante para minutos e segundos
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        # Formata o tempo no formato MM:SS
        timer_display.config(text=f"{minutes:02d}:{seconds:02d}")
        remaining_time -= 1
        # Agenda a função para ser chamada novamente após 1000 ms (1 segundo)
        root.after(1000, update_timer)
    elif remaining_time == 0:
        # Quando o tempo acabar, exibe uma mensagem
        timer_display.config(text="00:00")
        is_running = False
        messagebox.showinfo("Fim", "Horário de almoço encerrado!")

# Função para iniciar o cronômetro
def start_timer():
    global remaining_time, is_running
    try:
        # Obtém o tempo informado pelo usuário (em minutos)
        time_in_minutes = int(time_entry.get())
        if time_in_minutes <= 0:
            raise ValueError
        # Converte minutos para segundos
        remaining_time = time_in_minutes * 60
        is_running = True
        start_button.config(state=tk.DISABLED)  # Desabilita o botão de iniciar
        stop_button.config(state=tk.NORMAL)     # Habilita o botão de parar
        update_timer()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor válido (número inteiro positivo).")

# Função para parar o cronômetro
def stop_timer():
    global is_running
    is_running = False
    start_button.config(state=tk.NORMAL)  # Habilita o botão de iniciar
    stop_button.config(state=tk.DISABLED) # Desabilita o botão de parar

# Configurações iniciais
remaining_time = 0
is_running = False

# Cria a janela principal
root = tk.Tk()
root.title("Cronômetro de Almoço")
root.attributes('-zoomed', True)  # Abre a janela maximizada no Linux
root.resizable(True, True)  # Permite redimensionamento da janela


# Configura o layout da janela
root.configure(bg='#333333')  # Fundo escuro
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Frame principal para organizar os elementos
main_frame = tk.Frame(root, bg='#333333')
main_frame.grid(row=0, column=0, sticky="nsew")

# Texto "Em horário de almoço"
label_almoco = tk.Label(main_frame, text="Em horário de almoço", font=('Helvetica', 86), fg='white', bg='#333333')
label_almoco.grid(row=0, column=0, pady=(20, 10))

# Texto "Retorno em:"
label_retorno = tk.Label(main_frame, text="Retorno em:", font=('Helvetica', 60), fg='white', bg='#333333')
label_retorno.grid(row=1, column=0, pady=(10, 20))

# Exibição do cronômetro (centralizado)
timer_display = tk.Label(main_frame, text="00:00", font=('Helvetica', 72), fg='yellow', bg='#333333')
timer_display.grid(row=2, column=0, pady=(20, 40))

# Campo para inserir o tempo desejado (em minutos)
time_entry = tk.Entry(main_frame, font=('Helvetica', 24), justify='center')
time_entry.grid(row=3, column=0, pady=(10, 20))
time_entry.insert(0, "1")  # Valor padrão de 1 minuto

# Frame para os botões (Iniciar e Parar na mesma linha)
button_frame = tk.Frame(main_frame, bg='#333333')
button_frame.grid(row=4, column=0, pady=(10, 20))

# Botão para iniciar o cronômetro
start_button = tk.Button(button_frame, text="Iniciar", font=('Helvetica', 24), bg='green', fg='white', command=start_timer)
start_button.pack(side="left", padx=10)  # Coloca o botão à esquerda

# Botão para parar o cronômetro
stop_button = tk.Button(button_frame, text="Parar", font=('Helvetica', 24), bg='red', fg='white', command=stop_timer, state=tk.DISABLED)
stop_button.pack(side="left", padx=10)  # Coloca o botão à direita

# Botão para sair do programa
exit_button = tk.Button(main_frame, text="Sair", font=('Helvetica', 18), bg='gray', fg='white', command=root.destroy)
exit_button.grid(row=5, column=0, pady=(20, 10))

# Centraliza o frame na tela
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Inicia o loop principal da interface gráfica
root.mainloop()