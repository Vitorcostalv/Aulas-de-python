import threading
import time

def contar(nome, limite):
    for i in range(1, limite + 1):
        print(f"{nome} contando: {i}")
        time.sleep(1)

# Criando threads
thread1 = threading.Thread(target=contar, args=("Thread 1", 5))
thread2 = threading.Thread(target=contar, args=("Thread 2", 5))

# Iniciando as threads
thread1.start()
thread2.start()

# Esperando as threads terminarem
thread1.join()
thread2.join()

print("Contagem concluída!")
