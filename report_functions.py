'''
Conterá as funções para relatórios e estatísticas.
'''

import tkinter as tk
from tkinter import messagebox, simpledialog # <-- simpledialog já estava no seu comentário, mas garanto que está aqui

# Importa as variáveis de dados e funções auxiliares de outros módulos
import data_manager
from gui_elements import show_in_new_window


# =================================================================
# MÓDULO: FUNÇÕES DE RELATÓRIOS E ESTATÍSTICAS (REPORT FUNCTIONS)
#
# Este módulo contém funções para gerar diferentes tipos de
# relatórios e estatísticas sobre os eventos e participantes,
# ajudando os organizadores a analisar os dados.
#
# Conceitos Chave Adicionais (map e filter):
# - map(): Transforma cada item de uma coleção aplicando uma função.
#          Pense em "mapear" cada item para uma nova forma.
# - filter(): Seleciona itens de uma coleção que satisfazem uma condição.
#             Pense em "filtrar" itens que não se encaixam.
# - lambda: Funções anônimas (sem nome) pequenas, muito usadas com map e filter.
#
# Dependências:
# - `data_manager`: Para acessar `events_data` e `participants_data`.
# - `gui_elements`: Para exibir os relatórios em novas janelas.
# - `tkinter.messagebox`, `tkinter.simpledialog`: Para interações com o usuário.
# =================================================================

import tkinter as tk
from tkinter import messagebox

# Importa as variáveis de dados e funções auxiliares de outros módulos
import data_manager
from gui_elements import show_in_new_window

# -----------------------------------------------------------------
# Funções de Relatórios e Estatísticas
# -----------------------------------------------------------------

def generate_statistics():
    """
    Gera um relatório com estatísticas gerais do sistema, como:
    - Total de eventos
    - Total de participantes cadastrados
    - Top 5 participantes mais ativos (com mais inscrições)
    - Temas de eventos mais frequentes

    Processo:
    1. Calcula totais simples.
    
    2. Conta a participação por participante (`participant_event_counts`) usando compreensão de dicionário.
       Pense em: "Para cada participante em cada evento, conte quantos eventos ele está".
    
    3. Ordena os participantes pelo número de eventos para encontrar os mais ativos.
    
    4. Conta a frequência de temas (`theme_counts`) usando compreensão de dicionário.
       Pense em: "Para cada tema de evento, conte quantas vezes ele aparece".
       Counter como um contador de frequência. Dada uma lista de itens, ele retorna um objeto (que se comporta como um dicionário) 
        onde as chaves são os itens da lista e os valores são a quantidade de vezes que cada item apareceu (sua frequência).
    
    5. Ordena os temas pela frequência.
    
    6. Constrói uma string com todas as estatísticas e a exibe usando `map` para formatar as listagens.
    """
    stats_str = "--- Estatísticas do Sistema ---\n"
    
    total_events = len(data_manager.events_data) # Conta o número de eventos
    total_participants = len(data_manager.participants_data) # Conta o número de participantes globais
    
    stats_str += f"Total de Eventos: {total_events}\n"
    stats_str += f"Total de Participantes Cadastrados: {total_participants}\n"
    
    # ------------------------------------
    # Participantes mais ativos (inscritos em mais eventos)
    # Aprimorado: Primeiro, coleta todas as participações em uma lista plana de p_ids.
    all_p_ids_in_events = []
    for details in data_manager.events_data.values():
        all_p_ids_in_events.extend(details['participants']) #todos os IDs dessa lista são adicionados um por um ao final da lista all_p_ids_in_events.
    
    #.values() pega apenas os valores de todos os pares chave-valor presentes nesse dicionário.
    #extend() é usado para adicionar todos os itens de um iterável (lista,tupla,string) ao final da lista atual.
    
    # Usa a função Counter do módulo collections para contar rapidamente as ocorrências
    from collections import Counter
    participant_event_counts = Counter(all_p_ids_in_events)
    # participant_event_counts agora é um dicionário {ID_participante: contagem}
        # Counter({'P001': 3, 'P002': 2, 'P003': 1, 'P004': 1})
        
    if participant_event_counts: # Se houver participantes inscritos em eventos
        # Ordena os participantes pela contagem de eventos e pega os 5 primeiros
        most_active_items = sorted(participant_event_counts.items(), key=lambda item: item[1], reverse=True)[:5]
        
        
        
        stats_str += "\n--- Top 5 Participantes Mais Ativos ---\n"
    