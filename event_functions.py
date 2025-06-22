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
