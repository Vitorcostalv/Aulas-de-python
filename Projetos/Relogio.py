import tkinter as tk
import time
from datetime import datetime, timedelta
from threading import Thread

class RelogioApp:
    def __init__(self, master):
        self.master = master
        master.title("Relógio e Temporizador")
        master.geometry("400x300")

        # Mostrar o horário atual
        self.label_hora_atual = tk.Label(master, text="", font=("Helvetica", 16))
        self.label_hora_atual.pack(pady=10)
        self.atualizar_hora()

        # Contagem regressiva
        self.label_contagem_regressiva = tk.Label(master, text="Contagem Regressiva:", font=("Helvetica", 14))
        self.label_contagem_regressiva.pack(pady=10)

        self.entrada_tempo = tk.Entry(master, font=("Helvetica", 12))
        self.entrada_tempo.pack(pady=5)
        self.entrada_tempo.insert(0, "Formato: HH:MM:SS")

        self.botao_iniciar_contagem = tk.Button(master, text="Iniciar Contagem", command=self.iniciar_contagem_regressiva)
        self.botao_iniciar_contagem.pack(pady=5)

        self.label_tempo_restante = tk.Label(master, text="", font=("Helvetica", 14))
        self.label_tempo_restante.pack(pady=10)

        # Agendamento de horário
        self.label_agendamento = tk.Label(master, text="Agendar Alarme (HH:MM):", font=("Helvetica", 14))
        self.label_agendamento.pack(pady=10)

        self.entrada_agendamento = tk.Entry(master, font=("Helvetica", 12))
        self.entrada_agendamento.pack(pady=5)

        self.botao_agendar = tk.Button(master, text="Agendar Alarme", command=self.agendar_alarme)
        self.botao_agendar.pack(pady=5)

        self.label_alarme = tk.Label(master, text="", font=("Helvetica", 14))
        self.label_alarme.pack(pady=10)

         # Variáveis para controle
        self.contagem_ativa = False
        self.alarme_ativado = False

        def atualizar_hora(self):
        # Atualiza o horário atual na interface
        agora = datetime.now().strftime("%H:%M:%S")
        self.label_hora_atual.config(text=f"Hora atual: {agora}")
        self.master.after(1000, self.atualizar_hora)  # Atualiza a cada segundo
