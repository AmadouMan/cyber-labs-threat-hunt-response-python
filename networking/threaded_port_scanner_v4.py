import socket
import time
import threading
from queue import Queue

print("\n=== SOC Multi-Threaded Port Scanner v4 ===\n")

target = input("Enter target IP: ")
# On s'assure que le port de fin n'est pas inférieur au port de début
start_port = 1
end_port = int(input("Enter max port to scan: "))
threads_count = 50

q = Queue()
open_ports = []

def worker():
    while not q.empty():
        port = q.get()
        try:
            # Tout ce qui suit doit être indenté pour être DANS la boucle while
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)

            result = s.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN] {port}")
                open_ports.append(port)
            
            s.close()
        except:
            pass
        finally:
            # Indique à la file d'attente que la tâche est terminée
            q.task_done()

start_time = time.time()

# Remplissage de la file d'attente
for port in range(start_port, end_port + 1):
    q.put(port)

threads = []

# Lancement des threads
for i in range(threads_count):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

# Attente de la fin de tous les threads
for t in threads:
    t.join()

end_time = time.time()

print("\n====== Scan Summary ======")

if open_ports:
    print("Open ports:", sorted(open_ports))
else:
    print("No open ports detected")

print("Scan duration:", round(end_time - start_time, 2), "seconds")
