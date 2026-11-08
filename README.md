# TDE de Programacao Concorrente

Trabalho individual desenvolvido por **Kauan Moraes**.

- Linguagem: Python 3.10 ou superior
- Video no YouTube: **[adicionar o link do video aqui]**

## Como executar

Nao precisa instalar bibliotecas externas. Na raiz do repositorio, execute:

```bash
python parte1-filosofos/filosofos_ingenuo.py
python parte1-filosofos/filosofos_corrigido.py
python parte2-semaforo/semaforo.py
python -u parte3-deadlock/deadlock_travado.py
python parte3-deadlock/deadlock_corrigido.py
```

O parametro `-u` deixa a saida da versao travada sem buffer antes do encerramento forcado.

## Parte 1 - Jantar dos Filosofos

Na versao ingenua, cada um dos cinco filosofos pega primeiro o garfo da esquerda. Usei uma barreira para fazer todos chegarem ao mesmo ponto antes de tentarem pegar o segundo garfo. Assim, cada filosofo fica segurando um recurso e esperando pelo proximo, formando uma espera circular. O resultado e um deadlock com os cinco bloqueados.

Na versao corrigida, cada garfo recebe um numero e todos sempre pegam primeiro o garfo de menor indice e depois o de maior indice. Essa hierarquia quebra a condicao de espera circular de Coffman, pois nao e possivel formar um ciclo seguindo uma ordem global crescente. Cada filosofo faz cinco refeicoes e, no teste realizado, todos conseguiram comer cinco vezes. Isso demonstra progresso no experimento. Como o `Lock` do Python nao promete uma fila justa, a ausencia absoluta de inanicao nao e uma garantia formal para uma execucao sem limite, mas o numero finito de refeicoes permite verificar que todos concluem nesta simulacao.

Pseudocodigo da correcao:

```text
para cada filosofo:
    primeiro = menor indice entre os dois garfos
    segundo = maior indice entre os dois garfos
    repetir 5 vezes:
        pensar
        adquirir primeiro
        adquirir segundo
        comer
        liberar segundo
        liberar primeiro
```

Trecho do log:

```text
Diagnostico: 5 filosofos bloqueados: [0, 1, 2, 3, 4]

Resultado final da versao corrigida:
Filosofo 0 comeu 5 vezes
Filosofo 1 comeu 5 vezes
Filosofo 2 comeu 5 vezes
Filosofo 3 comeu 5 vezes
Filosofo 4 comeu 5 vezes
Ninguem travou, todo mundo conseguiu comer.
```

Os logs completos estao em [parte1-filosofos/logs-execucao.txt](parte1-filosofos/logs-execucao.txt).

## Parte 2 - Threads e semaforo

O programa cria 8 threads e cada uma tenta fazer 200.000 incrementos, entao o valor esperado e 1.600.000. Sem protecao, duas ou mais threads podem ler o mesmo valor e depois gravar resultados calculados a partir dessa leitura antiga. Uma gravacao sobrescreve a outra e incrementos sao perdidos.

Na versao corrigida, um `threading.Semaphore(1)` protege a operacao de leitura e escrita. Somente uma thread entra na secao critica por vez. A liberacao e a aquisicao do semaforo tambem estabelecem a sincronizacao necessaria para que a proxima thread observe o valor atualizado. O resultado fica correto, mas o tempo aumenta porque os incrementos passam a ser serializados e existe custo de sincronizacao. O semaforo padrao do Python tambem nao oferece garantia formal de ordem FIFO.

Resultados obtidos em 8 de novembro de 2026, com Python 3.13.3:

| Versao | Execucao | Esperado | Obtido | Tempo |
|---|---:|---:|---:|---:|
| Sem semaforo | 1 | 1.600.000 | 202.300 | 0,123 s |
| Sem semaforo | 2 | 1.600.000 | 400.500 | 0,124 s |
| Sem semaforo | 3 | 1.600.000 | 252.100 | 0,126 s |
| Com semaforo | 1 | 1.600.000 | 1.600.000 | 1,194 s |
| Com semaforo | 2 | 1.600.000 | 1.600.000 | 1,204 s |
| Com semaforo | 3 | 1.600.000 | 1.600.000 | 1,183 s |

O log esta em [parte2-semaforo/logs-execucao.txt](parte2-semaforo/logs-execucao.txt).

## Parte 3 - Deadlock

A versao travada usa dois locks. A Thread 1 pega `LOCK_A` e espera por `LOCK_B`, enquanto a Thread 2 pega `LOCK_B` e espera por `LOCK_A`. As quatro condicoes de Coffman aparecem:

1. exclusao mutua: cada lock pertence a somente uma thread por vez;
2. manter e esperar: cada thread mantem um lock enquanto pede o outro;
3. nao preempcao: um lock nao e retirado a forca da thread;
4. espera circular: T1 espera por T2 e T2 espera por T1.

Na correcao, as duas threads adquirem sempre `LOCK_A` e depois `LOCK_B`. A ordem global elimina a espera circular. Uma thread pode precisar aguardar, mas as duas terminam normalmente.

Trecho do log:

```text
T1: tentando pegar LOCK_B (vai travar aqui)
T2: tentando pegar LOCK_A (vai travar aqui)
!!! DEADLOCK !!!

As duas terminaram certinho em 0.10s
Sem deadlock!
```

Os logs completos estao em [parte3-deadlock/logs-execucao.txt](parte3-deadlock/logs-execucao.txt).

## Estrutura do repositorio

```text
parte1-filosofos/
  filosofos_ingenuo.py
  filosofos_corrigido.py
  logs-execucao.txt
parte2-semaforo/
  semaforo.py
  logs-execucao.txt
parte3-deadlock/
  deadlock_travado.py
  deadlock_corrigido.py
  logs-execucao.txt
README.md
```

