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





# -----------------------------------------------------------------
# 1. Armazenamento Principal de Dados
# -----------------------------------------------------------------

# Dicionário para armazenar informações dos eventos.
# A chave será o NOME do evento (sempre capitalizado para consistência).
# O valor será outro dicionário com os detalhes do evento:
# {
#   "Nome do Evento": {
#       "data": "AAAA-MM-DD",
#       "theme": "Tema do Evento",
#       "participants": ["ID_Participante_1", "ID_Participante_2"]
#   },
#   "Outro Evento": { ... }
# }

events_data = {}



# =================================================================

# Dicionário para armazenar informações dos participantes.
# A chave será o ID do participante (sempre em maiúsculas para consistência, ex: "P001").
# O valor será outro dicionário com os detalhes do participante:
# {
#   "P001": {
#       "name": "Nome do Participante",
#       "email": "email@example.com",
#       "preferences": "Preferências Temáticas"
#   },
#   "P002": { ... }
# }
participants_data = {}




# =================================================================

# Variável global que mantém o próximo número disponível para um novo ID de participante.
# Ex: Se for 1, o próximo ID será P001. Se for 10, o próximo será P010.
# Começa em 1 porque P000 não é comum.
next_participant_id_num = 1

