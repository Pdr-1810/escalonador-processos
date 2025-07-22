import time
from collections import deque
from Base_Escalonador1 import *
from Tarefas import *

class EscalonadorFIFO(EscalonadorCAV):

    def __init__(self, valor_sobrecarga=1):
        super().__init__(valor_sobrecarga)

    def escalonar(self):
        lista_execucao = []
        fila_chegada = deque(self.tarefas)
        contador = 0

        while lista_execucao or fila_chegada:
            while fila_chegada and fila_chegada[0].tempo_chegada <= contador:
                tarefa = fila_chegada.popleft()
                lista_execucao.append(tarefa)

            if lista_execucao:
                tarefa = lista_execucao[0]
                tempo_exec = tarefa.duracao
                tarefa.tempo_restante -= tempo_exec
                contador += tempo_exec
                print(f"Executando tarefa {tarefa.nome} por {tempo_exec} segundos.")
                time.sleep(tempo_exec)
                print(f"Tarefa {tarefa.nome} finalizada, tempo de espera: {contador - tarefa.tempo_chegada}")
                lista_execucao.pop(0)

            else:
                contador += 1

        self.exibir_sobrecarga()

if __name__ == "__main__":
    # Criar algumas tarefas fictícias
    tarefas = criar_tarefas()

    # Criar uns CAV
    cav1 = CAV(id=1)
    for t in tarefas:
        cav1.adicionar_tarefa(t)

    #Criar um escalonador FIFO 
    print("Simulando CAV com FIFO: \n")
    escalonador_FIFO= EscalonadorFIFO(2)
    for t in tarefas:
        escalonador_FIFO.adicionar_tarefa(t)
    
    simulador_pont = CAV(id=1)
    simulador_pont.executar_tarefas(escalonador_FIFO)