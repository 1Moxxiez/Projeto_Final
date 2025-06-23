'''
 Conterá as funções específicas para operações com eventos.
'''

# =================================================================
# MÓDULO: FUNÇÕES DE EVENTOS (EVENT FUNCTIONS)
#
# Este módulo contém todas as funções que permitem ao usuário
# interagir com os dados dos eventos: adicionar, remover, atualizar
# e exibir informações de eventos.
#
# Conceitos Chave Adicionais (map e filter):
# - map(): Transforma cada item de uma coleção aplicando uma função.
#          Pense em "mapear" cada item para uma nova forma.
# - filter(): Seleciona itens de uma coleção que satisfazem uma condição.
#             Pense em "filtrar" itens que não se encaixam.
# - lambda: Funções anônimas (sem nome) pequenas, muito usadas com map e filter.
#
# Dependências:
# - `data_manager`: Para acessar e modificar `events_data`.
# - `gui_elements`: Para exibir informações em novas janelas.
# - `tkinter.messagebox`, `tkinter.simpledialog`: Para interações com o usuário.
# =================================================================

import tkinter as tk
from tkinter import messagebox, simpledialog

# Importa as variáveis de dados e funções auxiliares de outros módulos
import data_manager
from gui_elements import show_in_new_window

# =================================================================
# Funções de Gerenciamento de Eventos
# =================================================================


# -----------------------------------------------------------------
# Exibir eventos
# -----------------------------------------------------------------
def display_events():
    """
    Exibe uma lista detalhada de todos os eventos cadastrados no sistema.

    Processo:
    1. Verifica se há eventos. Se não, informa o usuário.
    2. Usa `map` para transformar cada dicionário de evento em uma string formatada.
       Pense em: para cada 'figurinha de evento', crie um 'cartão de descrição'.
    3. Junta todos os 'cartões de descrição' em uma única string longa.
    4. Exibe esta string em uma nova janela de texto rolável.
    """
    
    if not data_manager.events_data: # Verifica se o dicionário de eventos está vazio
        messagebox.showinfo("Exibir Eventos", "Nenhum evento cadastrado.")
        return # Sai da função se não houver eventos
    
    # =================================================================
    # items() = É um método de dicionários que retorna uma lista de pares
    # (chave, valor). No nosso "álbum", ele te dá o nome da figurinha e a figurinha em si.
    
    # \n é um caractere especial que representa uma quebra de linha,
    # fazendo com que o próximo texto apareça na linha de baixo.
    # =================================================================
    
     # --- Usando map para formatar cada evento em uma string ---
    # map(funcao, iteravel) aplica 'funcao' a cada item do 'iteravel'.
    # Aqui, o iterável é data_manager.events_data.items(), que nos dá (name, details) para cada evento.
    # A função lambda é a "receita" de como formatar cada (item), par (name, details).
    # Ela retorna uma string formatada para cada evento.
    
    formatted_events = map(
        lambda item: (
            f"Nome: {item[0]}\n" # item[0] é o 'name' (chave do dicionário events_data)
            f"Data: {item[1]['data']}\n" # item[1] é o 'details' (valor do dicionário events_data), e acessamos a 'data' dentro dele
            f"Tema: {item[1]['theme']}\n"
            f"Participantes: {len(item[1]['participants'])}\n"
            f"------------------------" # Separador para cada evento, sem \n final aqui
        ),
        data_manager.events_data.items() #gera a tupla (chave, valor) --> item
    )
    # formatted_events é um ITERADOR, não uma lista. Ele vai gerar as strings sob demanda.

    # Junta todas as strings formatadas de eventos em uma única grande string.
    # '\n\n'.join(...) coloca duas quebras de linha entre cada bloco de evento.
    events_str = "--- Lista de Eventos ---\n\n" + "\n\n".join(formatted_events)
    
    show_in_new_window("Lista de Eventos", events_str) # Exibe o texto na nova janela
    