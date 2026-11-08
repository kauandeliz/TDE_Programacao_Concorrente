# TDE Programacao Concorrente

## Aluno

Kauan Moraes

Trabalho feito individualmente.

## Linguagem usada

Python 3.10 ou superior.

## Video

Link do video no YouTube: **COLOCAR O LINK AQUI**

## Como executar

Nao precisa instalar nenhuma biblioteca. Basta ter o Python instalado e executar os comandos abaixo na pasta do projeto:

```bash
python parte1-filosofos/filosofos_ingenuo.py
python parte1-filosofos/filosofos_corrigido.py
python parte2-semaforo/semaforo.py
python -u parte3-deadlock/deadlock_travado.py
python parte3-deadlock/deadlock_corrigido.py
```

Usei o `-u` no programa do deadlock para mostrar todas as mensagens antes de ele ser encerrado.

## Parte 1 - Jantar dos Filosofos

Nesta parte fiz duas versoes do problema do jantar dos filosofos.

Na primeira versao, cada filosofo pega um garfo e depois tenta pegar o outro. Como todos fazem isso ao mesmo tempo, cada um fica esperando o garfo que esta com o filosofo ao lado. Assim acontece o deadlock e nenhum deles consegue comer.

Na versao corrigida, coloquei uma ordem para pegar os garfos. O filosofo sempre pega primeiro o garfo com o menor numero e depois o de maior numero. Isso tira a espera circular e evita o deadlock.

Ordem usada no programa:

```text
pensar
pegar o garfo de menor numero
pegar o garfo de maior numero
comer
devolver os dois garfos
```

Resultado da versao com problema:

```text
Diagnostico: 5 filosofos bloqueados: [0, 1, 2, 3, 4]
```

Resultado da versao corrigida:

```text
Filosofo 0 comeu 5 vezes
Filosofo 1 comeu 5 vezes
Filosofo 2 comeu 5 vezes
Filosofo 3 comeu 5 vezes
Filosofo 4 comeu 5 vezes
Ninguem travou, todo mundo conseguiu comer.
```

O log esta no arquivo [parte1-filosofos/logs-execucao.txt](parte1-filosofos/logs-execucao.txt).

## Parte 2 - Semaforo

Nesta parte usei 8 threads. Cada uma faz 200.000 incrementos em um contador. Por isso, o resultado correto deveria ser 1.600.000.

Sem o semaforo, varias threads tentam alterar o contador ao mesmo tempo. Algumas leem o mesmo valor e acabam sobrescrevendo o resultado uma da outra. Por isso varios incrementos sao perdidos.

Com o semaforo, somente uma thread altera o contador por vez. O resultado fica correto nas tres tentativas. A parte ruim e que o programa demora mais, porque as threads precisam esperar a vez delas.

### Resultados

| Versao | Tentativa | Esperado | Resultado | Tempo |
|---|---:|---:|---:|---:|
| Sem semaforo | 1 | 1.600.000 | 202.300 | 0,123 s |
| Sem semaforo | 2 | 1.600.000 | 400.500 | 0,124 s |
| Sem semaforo | 3 | 1.600.000 | 252.100 | 0,126 s |
| Com semaforo | 1 | 1.600.000 | 1.600.000 | 1,194 s |
| Com semaforo | 2 | 1.600.000 | 1.600.000 | 1,204 s |
| Com semaforo | 3 | 1.600.000 | 1.600.000 | 1,183 s |

O log completo esta no arquivo [parte2-semaforo/logs-execucao.txt](parte2-semaforo/logs-execucao.txt).

## Parte 3 - Deadlock

Nesta parte usei duas threads e dois locks chamados `LOCK_A` e `LOCK_B`.

Na versao que trava, a Thread 1 pega o LOCK_A e tenta pegar o LOCK_B. Ao mesmo tempo, a Thread 2 pega o LOCK_B e tenta pegar o LOCK_A. Uma fica esperando a outra e nenhuma consegue terminar.

As quatro condicoes do deadlock aparecem no programa:

- exclusao mutua: um lock so pode ficar com uma thread por vez;
- manter e esperar: a thread segura um lock enquanto espera o outro;
- sem preempcao: o lock nao e tirado da thread;
- espera circular: uma thread fica esperando a outra.

Para corrigir, fiz as duas threads pegarem os locks na mesma ordem: primeiro o LOCK_A e depois o LOCK_B. Dessa forma nao acontece mais a espera circular.

Resultado da versao travada:

```text
T1: tentando pegar LOCK_B (vai travar aqui)
T2: tentando pegar LOCK_A (vai travar aqui)
!!! DEADLOCK !!!
```

Resultado da versao corrigida:

```text
As duas terminaram certinho em 0.10s
Sem deadlock!
```

O log esta no arquivo [parte3-deadlock/logs-execucao.txt](parte3-deadlock/logs-execucao.txt).

## Pastas do trabalho

```text
parte1-filosofos
parte2-semaforo
parte3-deadlock
```
