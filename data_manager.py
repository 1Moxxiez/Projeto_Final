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






def set_initial_participant_id_counter():
    """
    Ajusta o contador de ID do participante após carregar dados (ex: de mock data).
    Isso garante que novos IDs gerados automaticamente não entrem em conflito
    com IDs já existentes, começando do maior ID + 1.
    """
    global next_participant_id_num# Indica que vamos modificar essa variável global.
    if participants_data: # Verifica se já existem participantes carregados
        max_id_num = 0 # Guarda o maior número de crachá que eu encontrei até agora. Começa em zero.
        
        # Percorre a chave do particiipante_data - todos os IDs de participantes existentes
        for p_id in participants_data.keys():
            try:
                # Verifica se o ID começa com 'P' e se o restante é um número
                # "Para cada crachá, eu tento tirar a letra 'P' e converter o resto para um número."
                # Exemplo: 'P006'
                # p_id.startswith('P'): "Começa com 'P'?" -> Sim!
                # p_id[1:]: "Pego o resto do crachá, que é '006'."
                # .isdigit(): "É tudo número?" -> Sim!
                if p_id.startswith('P') and p_id[1:].isdigit():
                    num_part = int(p_id[1:])
                    # Se este número for maior que o máximo encontrado até agora, atualiza o máximo
                    if num_part > max_id_num:
                        max_id_num = num_part
                        
            except ValueError: # <--- Se a linha acima der ValueError
                # Então, o Python vem para cá.
                # 'pass' significa "não faça nada, apenas continue o programa".
                pass
        # Define o próximo ID como o maior ID encontrado + 1
        next_participant_id_num = max_id_num + 1
    
    else:
        # Se não houver participantes, o contador começa em 1.
        next_participant_id_num = 1
        
    
    
# -----------------------------------------------------------------
# 3. Importação de Dados de Exemplo (Mock Data)
# -----------------------------------------------------------------

# (Depende de tkinter para messagebox, então será chamada do main.py ou passada como argumento)
# Esta função simula o carregamento de dados de arquivos .py
# Em um sistema real, você leria esses dados de arquivos ou de um banco de dados e  ia só apaga td.
def import_mock_data_internal():
    """
    Simula a importação de dados de eventos e participantes.
    Carrega dados de exemplo para os dicionários `events_data` e `participants_data`.
    """
    # Usamos 'global' para indicar que estamos acessando e modificando as variáveis globais
    # `events_data`, `participants_data` e `next_participant_id_num` definidas acima.
    global events_data, participants_data

    # Limpa os dados existentes antes de carregar os novos, para evitar duplicatas ao importar
    # múltiplas vezes (se o sistema permitisse).
    events_data.clear()
    participants_data.clear()

# -----------------------------------------------------------------
# 1.  Dados de exemplo de eventos.
# -----------------------------------------------------------------

    #  nomes já estão aqui com a primeira letra maiúscula para demonstrar a consistência.
    mock_events = [
        {"name": "Workshop de IA", "data": "2025-07-10", "theme": "Inteligência Artificial", "participants": ["P001", "P002", "P003"]},
        {"name": "Maratona de Programação", "data": "2025-08-15", "theme": "Programação", "participants": ["P001", "P004"]},
        {"name": "Palestra sobre Cibersegurança", "data": "2025-09-01", "theme": "Segurança", "participants": ["P002", "P005", "P006"]},
        {"name": "Mini-curso de Webdev", "data": "2025-10-20", "theme": "Web", "participants": ["P003", "P004"]},
        {"name": "Hackathon Inovação", "data": "2025-11-05", "theme": "Inovação", "participants": []},
        {"name": "Workshop de Redes", "data": "2025-07-25", "theme": "Redes", "participants": ["P001", "P002"]}
    ]
    
    
# -----------------------------------------------------------------
# 2.  Dados de exemplo de eventos.
# -----------------------------------------------------------------

    # IDs já em maiúsculas e nomes capitalizados.
    mock_participants = [
        {"id": "P001", "name": "Alice Silva", "email": "alice@email.com", "preferences": "IA, Programação"},
        {"id": "P002", "name": "Bruno Costa", "email": "bruno@email.com", "preferences": "Segurança, Redes"},
        {"id": "P003", "name": "Carla Dias", "email": "carla@email.com", "preferences": "IA, Web"},
        {"id": "P004", "name": "Daniel Evangelista", "email": "daniel@email.com", "preferences": "Programação, Web"},
        {"id": "P005", "name": "Eduarda Fernandes", "email": "eduarda@email.com", "preferences": "Segurança"},
        {"id": "P006", "name": "Felipe Garcia", "email": "felipe@email.com", "preferences": "Segurança"},
    ]

# -----------------------------------------------------------------
# Preenche o dicionário `events_data` com os dados de exemplo
# -----------------------------------------------------------------

    for even