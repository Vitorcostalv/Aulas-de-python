import tkinter as tk
import time
from datetime import datetime
from threading import Thread

class RelogioApp:
    def __init__(self, master):
        self.master = master
        master.title("Relógio e Temporizador")
        master.geometry("800x600")
        master.configure(bg="black")  # Fundo preto

        # Mostrar o horário atual
        self.label_hora_atual = tk.Label(master, text="", font=("Helvetica", 16), fg="light gray", bg="black")
        self.label_hora_atual.pack(pady=10)
        self.atualizar_hora()

        # Contagem regressiva
        self.label_contagem_regressiva = tk.Label(master, text="Contagem Regressiva:", font=("Helvetica", 14), fg="light gray", bg="black")
        self.label_contagem_regressiva.pack(pady=10)

        self.entrada_tempo = tk.Entry(master, font=("Helvetica", 12), fg="black", bg="light gray")
        self.entrada_tempo.pack(pady=5)
        self.entrada_tempo.insert(0, "Formato: HH:MM:SS")

        self.botao_iniciar_contagem = tk.Button(master, text="Iniciar Contagem", command=self.iniciar_contagem_regressiva, fg="black", bg="light gray")
        self.botao_iniciar_contagem.pack(pady=5)

        self.label_tempo_restante = tk.Label(master, text="", font=("Helvetica", 14), fg="light gray", bg="black")
        self.label_tempo_restante.pack(pady=10)

        # Agendamento de horário
        self.label_agendamento = tk.Label(master, text="Agendar Alarme (HH:MM):", font=("Helvetica", 14), fg="light gray", bg="black")
        self.label_agendamento.pack(pady=10)

        self.entrada_agendamento = tk.Entry(master, font=("Helvetica", 12), fg="black", bg="light gray")
        self.entrada_agendamento.pack(pady=5)

        self.botao_agendar = tk.Button(master, text="Agendar Alarme", command=self.agendar_alarme, fg="black", bg="light gray")
        self.botao_agendar.pack(pady=5)

        # Lista de alarmes agendados
        self.label_agendamentos = tk.Label(master, text="Agendamentos:", font=("Helvetica", 14), fg="light gray", bg="black")
        self.label_agendamentos.pack(pady=10)

        self.lista_agendamentos = tk.Listbox(master, font=("Helvetica", 12), fg="black", bg="light gray", height=5)
        self.lista_agendamentos.pack(pady=5)

        # Variáveis para controle
        self.contagem_ativa = False
        self.alarme_ativado = False
        self.alarmes_agendados = []

    def atualizar_hora(self):
        # Atualiza o horário atual na interface
        agora = datetime.now().strftime("%H:%M:%S")
        self.label_hora_atual.config(text=f"Hora atual: {agora}")
        self.master.after(1000, self.atualizar_hora)  # Atualiza a cada segundo

    def iniciar_contagem_regressiva(self):
        if not self.contagem_ativa:
            tempo_str = self.entrada_tempo.get()
            try:
                h, m, s = map(int, tempo_str.split(":"))
                total_segundos = h * 3600 + m * 60 + s
                self.contagem_ativa = True
                Thread(target=self.contagem_regressiva, args=(total_segundos,)).start()
            except ValueError:
                self.label_tempo_restante.config(text="Formato inválido! Use HH:MM:SS")

    def contagem_regressiva(self, total_segundos):
        # Função de contagem regressiva
        while total_segundos > 0 and self.contagem_ativa:
            mins, secs = divmod(total_segundos, 60)
            hours, mins = divmod(mins, 60)
            tempo_formatado = f"{hours:02d}:{mins:02d}:{secs:02d}"
            self.label_tempo_restante.config(text=tempo_formatado)
            time.sleep(1)
            total_segundos -= 1

        if self.contagem_ativa:
            self.label_tempo_restante.config(text="Tempo esgotado!")
        self.contagem_ativa = False

    def agendar_alarme(self):
        horario_alarme = self.entrada_agendamento.get()
        try:
            # Converte o horário para o formato de hora e minuto
            horario_alarme = datetime.strptime(horario_alarme, "%H:%M").time()
            
            # Adiciona o alarme na lista de alarmes agendados
            self.alarmes_agendados.append(horario_alarme.strftime("%H:%M"))
            self.lista_agendamentos.insert(tk.END, f"Agendamento marcado para {horario_alarme.strftime('%H:%M')}")

            # Ativa o alarme e verifica se o horário foi atingido
            self.alarme_ativado = True
            Thread(target=self.verificar_alarme, args=(horario_alarme,)).start()
        except ValueError:
            self.lista_agendamentos.insert(tk.END, "Formato inválido! Use HH:MM")

    def verificar_alarme(self, horario_alarme):
        # Verifica continuamente se o horário atual coincide com o horário do alarme
        while self.alarme_ativado:
            agora = datetime.now().time().replace(second=0, microsecond=0)
            if agora == horario_alarme:
                self.lista_agendamentos.insert(tk.END, f"ALARM!!! {horario_alarme.strftime('%H:%M')}")  # Adiciona o alarme tocado à lista
                self.alarme_ativado = False
                break
            time.sleep(30)  # Verifica a cada 30 segundos

# Cria a janela principal
janela = tk.Tk()
app = RelogioApp(janela)
janela.mainloop()
