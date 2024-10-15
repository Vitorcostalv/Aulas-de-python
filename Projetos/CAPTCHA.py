import tkinter as tk
import random
import string

def gerar_captcha(tamanho=6):
    # Gera um CAPTCHA aleatório com letras e números
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def verificar_captcha():
    # Verifica se o CAPTCHA inserido está correto
    if entrada_captcha.get() == captcha_atual:
        label_resultado.config(text="ACESSO LIBERADO", fg="green")
        botao_verificar.config(state=tk.DISABLED)
        botao_novo_captcha.config(state=tk.DISABLED)
    else:
        label_resultado.config(text="CAPTCHA incorreto. Tente novamente.", fg="red")
        entrada_captcha.delete(0, tk.END)

def gerar_novo_captcha():
    # Gera um novo CAPTCHA e atualiza o display
    global captcha_atual
    captcha_atual = gerar_captcha()
    label_captcha.config(text=captcha_atual)
    entrada_captcha.delete(0, tk.END)
    label_resultado.config(text="")
    botao_verificar.config(state=tk.NORMAL)
    botao_novo_captcha.config(state=tk.NORMAL)

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("CAPTCHA Generator")
janela.geometry("300x250")

captcha_atual = gerar_captcha()

# Labels e entradas
label_instrucoes = tk.Label(janela, text="Digite o CAPTCHA abaixo:")
label_instrucoes.pack(pady=10)

label_captcha = tk.Label(janela, text=captcha_atual, font=("Helvetica", 24, "bold"))
label_captcha.pack(pady=5)

entrada_captcha = tk.Entry(janela, font=("Helvetica", 14))
entrada_captcha.pack(pady=5)

botao_verificar = tk.Button(janela, text="Verificar", command=verificar_captcha)
botao_verificar.pack(pady=5)

botao_novo_captcha = tk.Button(janela, text="Novo CAPTCHA", command=gerar_novo_captcha)
botao_novo_captcha.pack(pady=5)

label_resultado = tk.Label(janela, text="", font=("Helvetica", 12))
label_resultado.pack(pady=10)

# Inicia o loop principal da interface
janela.mainloop()
