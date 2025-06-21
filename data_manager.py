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

# -----------------------------------------------------------------
# 2. Funções de Suporte ao Gerenciamento de Dados
# -----------------------------------------------------------------

def generate_next_participant_id():
    """
    ALGORITMO 1: Geração de ID Automático (Seqüencial e Formatado)

    Objetivo: Criar um ID único e fácil de ler para cada novo participante.
    Como Funciona (A "Receita" para o ID):
    1. Acessa o contador global de IDs (`next_participant_id_num`).
    
    2. Cria o novo ID formatado como "P" seguido de 3 dígitos (ex: P001, P015, P123).
       - `f"P{next_participant_id_num:03d}"`: Isso é uma f-string (string formatada).
         - `P`: É um prefixo fixo.
         - `{next_participant_id_num:03d}`: Pega o valor do contador e o formata:
           - `:03d`: Garante que o número tenha pelo menos 3 dígitos, preenchendo com zeros à esquerda se necessário
                     (ex: 1 vira 001, 15 vira 015). O 'd' indica que é um número inteiro.
    
    3. Converte o ID resultante para letras MAIÚSCULAS (`.upper()`) para padronização (ex: "p001" vira "P001").
    
    4. Incrementa o contador global para que o próximo ID gerado seja diferente.
    
    5. Retorna o ID recém-gerado.

    Lembrete: Pense nisso como um "gerador de senhas únicas" para participantes,
              mas que são numéricas e em sequência.
    """
    
    global next_participant_id_num # Indica que estamos modificando a variável global, não criando uma local
    new_id = f'P{next_participant_id_num:03d}'
    next_participant_id_num += 1
    return new_id