import threading
import time

LOCK_A = threading.Lock()
LOCK_B = threading.Lock()


def thread1():
    print("T1: pegando LOCK_A")
    LOCK_A.acquire()
    print("T1: peguei LOCK_A")

    time.sleep(0.05)

    print("T1: pegando LOCK_B")
    LOCK_B.acquire()
    print("T1: peguei LOCK_B")

    print("T1: terminei!")
    LOCK_B.release()
    LOCK_A.release()


def thread2():
    
    print("T2: pegando LOCK_A")
    LOCK_A.acquire()
    print("T2: peguei LOCK_A")

    time.sleep(0.05)

    print("T2: pegando LOCK_B")
    LOCK_B.acquire()
    print("T2: peguei LOCK_B")

    print("T2: terminei!")
    LOCK_B.release()
    LOCK_A.release()


def main():
    print("Deadlock versao corrigida (mesma ordem pras duas)\n")

    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)

    inicio = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    fim = time.time()

    print(f"\nAs duas terminaram certinho em {fim - inicio:.2f}s")
    print("Sem deadlock!")


if __name__ == "__main__":
    main()