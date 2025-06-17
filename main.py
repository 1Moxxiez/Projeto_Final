'''
O arquivo principal que iniciará a aplicação Tkinter e reunirá todas as partes.
'''

# =================================================================
# Este é o ponto de entrada da aplicação. Ele inicializa a janela
# principal do Tkinter, configura a interface do usuário (botões e menus),
# e "conecta" as ações do usuário às funções lógicas definidas nos outros módulos.
#
# Conceitos Chave:
# - Tkinter: Criação da janela principal e widgets (Label, Button, Menu).
# - Importação de Módulos: Como diferentes partes do código se comunicam.
# - Estrutura da GUI: Organização de elementos na tela.
# =================================================================

import tkinter as tk # Para criar interfaces gráficas
from tkinter import messagebox # Para exibir mensagens pop-up

# Importa os módulos que contêm as funções lógicas e de dados
import data_manager       # Gerencia os dados
import gui_elements       # Funções de interface (como nova janela de texto)
import event_functions    # Funções para eventos
import participant_functions # Funções para participantes
import report_functions   # Funções para relatórios e estatísticas


# -----------------------------------------------------------------
# 1. Configuração da Janela Principal (Root Window)
# -----------------------------------------------------------------

# Cria a janela principal da aplicação Tkinter.
# `Tk()` é a classe que representa a janela raiz de uma aplicação GUI.

root = tk.Tk()  #root (que significa "raiz" em inglês) é o nome padrão dado à janela principal
root.title('Sstea de Gerenciaento de Eventos da Comunidade Tech')