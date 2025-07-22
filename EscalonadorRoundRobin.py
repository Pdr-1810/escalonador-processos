import time
from collections import deque
from Base_Escalonador1 import *
from Tarefas import *

class EscalonadorRoundRobin(EscalonadorCAV):

    def __init__(self, quantum, valor_sobrecarga=1):
        super().__init__(valor_sobrecarga)
        self.quantum = quantum

    def escalonar(self):
        lista_execucao = []
        fila_chegada = deque(self.tarefas)
        contador = 0

        while lista_execucao or fila_chegada:

            if lista_execucao and lista_execucao[0].tempo_restante == 0:
                tarefa_finalizada = lista_execucao.pop(0)
                print(f"Tarefa {tarefa_finalizada.nome} finalizada cumprindo a prioridade, tempo de resposta: {contador - tarefa_finalizada.tempo_chegada}")

            while fila_chegada and fila_chegada[0].tempo_chegada <= contador:
                tarefa = fila_chegada.popleft()
                lista_execucao.append(tarefa)

            if lista_execucao:
                tarefa = lista_execucao[0]
                if tarefa.tempo_restante > 0:
                    tempo_exec = min(tarefa.tempo_restante, self.quantum)
                    tarefa.tempo_restante -= tempo_exec
                    contador += tempo_exec
                    print(f"Executando tarefa {tarefa.nome} por {tempo_exec} segundos.")
                    time.sleep(tempo_exec)

                    if tarefa.tempo_restante > 0:
                        temp = lista_execucao.pop(0)
                        self.registrar_sobrecarga(self.valor_sobrecarga)
                        contador += self.valor_sobrecarga
                        lista_execucao.append(temp)

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

    #Criar um escalonador RoundRobin 
    print("Simulando CAV com RoundRobin: \n")
    escalonador_rr= EscalonadorRoundRobin(2)
    for t in tarefas:
        escalonador_rr.adicionar_tarefa(t)
    
    simulador_pont = CAV(id=1)
    simulador_pont.executar_tarefas(escalonador_rr)