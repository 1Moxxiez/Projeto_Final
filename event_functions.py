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

# -----------------------------------------------------------------
# Funções de Gerenciamento de Eventos
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