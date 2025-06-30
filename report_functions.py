'''
Conterá as funções para relatórios e estatísticas.
'''
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
# - `collections import Counter`, `collections`: Para funcionalidades de contagem avançada (como Counter).
# =================================================================

import tkinter as tk # Para criar interfaces gráficas
from tkinter import messagebox

from collections import Counter

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
    # Aprimorado: Primeiro, coleta todas as participações em uma lista de p_ids.
    all_p_ids_in_events = []
    for details in data_manager.events_data.values():
        all_p_ids_in_events.extend(details['participants']) #todos os IDs dessa lista são adicionados um por um ao final da lista all_p_ids_in_events.
    
    #.values() pega apenas os valores de todos os pares chave-valor presentes nesse dicionário.
    #extend() é usado para adicionar todos os itens de um iterável (lista,tupla,string) ao final da lista atual.
    
    
    # Usa a função Counter do módulo collections para contar rapidamente as ocorrências
    participant_event_counts = Counter(all_p_ids_in_events)
    # participant_event_counts agora é um dicionário {ID_participante: contagem}
        # Counter({'P001': 3, 'P002': 2, 'P003': 1, 'P004': 1})
        
    if participant_event_counts: # Se houver participantes inscritos em eventos
        # Ordena os participantes pela contagem de eventos e pega os 5 primeiros
        most_active_items = sorted(participant_event_counts.items(), key=lambda item: item[1], reverse=True)[:5]  #é uma lista de tuplas
        '''
        key= (Argumento): É um argumento opcional da função sorted(). 
        Ele especifica uma função (lambda) que será usada para extrair um valor de cada item da coleção antes de compará-los para a ordenação. 
        É como dizer: "Não ordene pelo item inteiro, ordene por esta 'chave' específica dentro de cada item".

        True: Significa que a ordenação deve ser feita em ordem decrescente (do maior para o menor). Se fosse 
        
        [:5]: É uma operação de fatiamento de lista (slicing), aplicada depois que sorted() retorna a lista já ordenada.
        propósito: Seleciona os primeiros 5 elementos da lista resultante. É assim que você obtém o "Top 5" participantes ou temas. 
        '''        
        
        
        stats_str += "\n--- Top 5 Participantes Mais Ativos ---\n"
        
        
        # Itera diretamente sobre os pares (p_id, count_events) já ordenados.
        # Obtém o nome do participante dentro da própria formatação.
        formatted_active_participants = [
            f"ID: {p_id}, Nome: {data_manager.participants_data.get(p_id, {}).get('name', 'Desconhecido')}, Eventos: {count_events}"
            for p_id, count_events in most_active_items
        ]
        stats_str += "\n".join(formatted_active_participants) + "\n"
        '''
        "\n".join(...):

        Ele pega uma lista de strings (ou qualquer outro iterável de strings).

        Ele junta todas essas strings em uma única string maior.

        E entre cada uma das strings originais, ele insere o caractere de quebra de linha (\n).
        '''
    else:
        stats_str += "\nNenhum participante em eventos para calcular os mais ativos.\n"
    
    
    
    # ------------------------------------
    # Temas mais frequentes
    all_themes = [details['theme'] for details in data_manager.events_data.values()]
    theme_counts = Counter(all_themes)
    
    if theme_counts:
        most_frequent_themes_items = sorted(theme_counts.items(), key=lambda item: item[1], reverse=True)  #é uma lista de tuplas
        
        
        stats_str += "\n--- Temas Mais Frequentes ---\n"
        
        
        formatted_frequent_themes = map(
            lambda item: f"Tema: {item[0]}, Eventos: {item[1]}",
            most_frequent_themes_items
        )
        stats_str += "\n".join(formatted_frequent_themes) + "\n"
    else:
        stats_str += "\nNenhum tema de evento para calcular os mais frequentes.\n"
    
    stats_str += "--------------------------------------"
    
    show_in_new_window("Estatísticas", stats_str)
