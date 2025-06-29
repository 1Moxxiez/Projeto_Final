'''
Conterá as funções específicas para operações com participantes.
'''

# participant_functions.py

# =================================================================
# MÓDULO: FUNÇÕES DE PARTICIPANTES (PARTICIPANT FUNCTIONS)
#
# Este módulo contém todas as funções que permitem ao usuário
# interagir com os dados dos participantes: adicionar, remover,
# atualizar, buscar e listar.
#
# Dependências:
# - `data_manager`: Para acessar e modificar `participants_data` e `events_data`.
# - `gui_elements`: Para exibir informações em novas janelas.
# - `tkinter.messagebox`, `tkinter.simpledialog`: Para interações com o usuário.
# =================================================================

import tkinter as tk
from tkinter import messagebox, simpledialog

# Importa as variáveis de dados e funções auxiliares de outros módulos
import data_manager
from gui_elements import show_in_new_window

# -----------------------------------------------------------------
# Funções de Gerenciamento de Participantes
# -----------------------------------------------------------------

# ALGORITMO 2: Adição de Participante (com ID Automático)