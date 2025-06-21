'''
Gerenciará os dados (eventos e participantes) e a lógica de persistência (simulada).
'''
import tkinter as tk
from tkinter import messagebox # Para exibir mensagens pop-up

# =================================================================
# MÓDULO: GERENCIAMENTO DE DADOS (DATA MANAGER)
#
# Este módulo é responsável por armazenar e gerenciar os dados
# de todos os eventos e participantes do sistema.
# Ele funciona como um banco de dados em memória simples,
# utilizando dicionários Python para guardar as informações.
#
# Conceitos Chave:
# - Variáveis Globais: `events_data`, `participants_data`, `next_participant_id_num`
# - Dicionários Python: Usados para organizar os dados por chaves únicas (nomes de eventos, IDs de participantes).
# - Geração de IDs Sequenciais: Garante que cada novo participante tenha um ID único e fácil de rastrear.
# =================================================================
