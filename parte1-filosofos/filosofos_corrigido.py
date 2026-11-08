import random
import threading
import time

N = 5
REFEICOES = 5  

garfos = [threading.Lock() for _ in range(N)]
vezes_que_comeu = [0] * N


def filosofo(i):
    garfo_esq = i
    garfo_dir = (i + 1) % N

    primeiro = min(garfo_esq, garfo_dir)
    segundo = max(garfo_esq, garfo_dir)

    for vez in range(REFEICOES):
        print(f"Filosofo {i}: pensando ({vez+1}/{REFEICOES})")
        time.sleep(random.uniform(0.05, 0.2))

        print(f"Filosofo {i}: com fome, vou pegar garfo {primeiro} primeiro")
        garfos[primeiro].acquire()

        print(f"Filosofo {i}: peguei garfo {primeiro}, agora vou pegar {segundo}")
        garfos[segundo].acquire()

        print(f"Filosofo {i}: comendo ({vez+1}/{REFEICOES})")
        vezes_que_comeu[i] += 1
        time.sleep(random.uniform(0.05, 0.15))

        garfos[segundo].release()
        garfos[primeiro].release()
        print(f"Filosofo {i}: terminei e devolvi os garfos")

    print(f"Filosofo {i}: acabei minhas {REFEICOES} refeicoes!")


def main():
    print("Jantar dos Filosofos_versao corrigida \n")

    threads = []
    for i in range(N):
        t = threading.Thread(target=filosofo, args=(i,))
        threads.append(t)

    inicio = time.time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    fim = time.time()

    print("\n Resultado final do jantar dos filosofos:")
    print(f"Demorou {fim - inicio:.2f} segundos")
    for i in range(N):
        print(f"Filosofo {i} comeu {vezes_que_comeu[i]} vezes")
    print("\nNinguem travou, todo mundo conseguiu comer.")


if __name__ == "__main__":
    main()