'''
Conterá as funções para relatórios e estatísticas.
'''

# report_functions.py

import tkinter as tk
from tkinter import messagebox, simpledialog # <--- ADICIONE simpledialog AQUI!

# Importa as variáveis de dados e funções auxiliares de outros módulos
import data_manager
from gui_elements import show_in_new_window

# ... o restante do seu código report_functions.py

# report_functions.py

# =================================================================
# MÓDULO: FUNÇÕES DE RELATÓRIOS E ESTATÍSTICAS (REPORT FUNCTIONS)
#
# Este módulo contém funções para gerar diferentes tipos de
# relatórios e estatísticas sobre os eventos e participantes,
# ajudando os organizadores a analisar os dados.
#
# Dependências:
# - `data_manager`: Para acessar `events_data` e `participants_data`.
# - `gui_elements`: Para exibir os relatórios em novas janelas.
# - `tkinter.messagebox`: Para mensagens de informação.
# =================================================================

import tkinter as tk
from tkinter import messagebox

# Importa as variáveis de dados e funções auxiliares de outros módulos
import data_manager
from gui_elements import show_in_new_window

# -----------------------------------------------------------------
# Funções de Relatórios e Estatísticas
# -----------------------------------------------------------------