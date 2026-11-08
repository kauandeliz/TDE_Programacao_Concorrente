import threading

N = 5

def main():
    forks = [threading.Lock() for _ in range(N)]
    barrier = threading.Barrier(N)

    def philosopher(i):
        left, right = i, (i + 1) % N

        print(f'Filósofo {i}: pensando', flush=True)
        print(f'Filósofo {i}: com fome', flush=True)

        forks[left].acquire()
        print(f'Filósofo {i}: adquiriu garfo {left}', flush=True)

        # Todos seguram o primeiro garfo
        # antes de tentar adquirir o segundo.
        barrier.wait()

        print(f'Filósofo {i}: esperando garfo {right}', flush=True)

        # A espera circular impede o progresso.
        forks[right].acquire()

        print(f'Filósofo {i}: comendo', flush=True)

        forks[right].release()
        forks[left].release()

    threads = [
        threading.Thread(
            target=philosopher,
            args=(i,),
            daemon=True
        )
        for i in range(N)
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join(timeout=0.5)

    blocked = [
        i for i, t in enumerate(threads)
        if t.is_alive()
    ]

    print(
        f'Diagnóstico: {len(blocked)} filósofos bloqueados: {blocked}',
        flush=True
    )

    print(
        'O processo principal termina para permitir '
        'a demonstração sem travar o terminal.'
    )


if __name__ == '__main__':
    main()
