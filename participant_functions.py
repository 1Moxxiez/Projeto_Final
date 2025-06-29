'''
Conterá as funções específicas para operações com participantes.
'''

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



# -----------------------------------------------------------------
# Adição de Participante (com ID Automático)
# -----------------------------------------------------------------
def add_new_participant_data(p_id=None):
    """
    Permite cadastrar um novo participante no sistema.
    Pode gerar um ID automaticamente ou usar um ID fornecido (para casos específicos).

    Processo:
    1. **Decide o ID:**
       - Se `p_id` NÃO for fornecido (ou seja, `None`), a função chama o
         `data_manager.generate_next_participant_id()` (o "Contador Global do ID")
         para obter um ID novo e único automaticamente. Exibe este ID ao usuário.
         
       - Se `p_id` FOR fornecido, ele é usado (mas é convertido para MAIÚSCULAS
         para padronização, usando `.upper()`).
         
    2. **Verifica Duplicidade:** Confere se o ID (automático ou manual) já existe
       no `data_manager.participants_data`. Se sim, informa e cancela.
       
    3. **Coleta Dados:** Solicita ao usuário o Nome Completo, E-mail e Preferências Temáticas.
       - `.capitalize()` para o nome: Garante que a primeira letra seja maiúscula.
       
    4. **Registra:** Adiciona as informações do novo participante ao dicionário
       `data_manager.participants_data`, usando o ID como chave.
       
    5. **Confirma:** Exibe uma mensagem de sucesso, incluindo o ID e o nome do participante.

    Lembrete: Este é o "Recrutador Inteligente" que ou cria um crachá novo ou
              confere um que você já tem para registrar a pessoa.
    """
    if p_id is None:
        p_id = data_manager.generate_next_participant_id()
        messagebox.showinfo("Novo ID participante",f"O ID gerado automaticamente para o novo participante é: {p_id}")
    else:
        p_id = p_id.upper
        
    if p_id in data_manager.participants_data:
        messagebox.showerror('Erro',f'ID de participante '{p_id}' já existe.')
        return

    name_input = simpledialog.askstring("Cadastrar Participante",f'Nome Completo para ID {p_id}:')
    if not name_input: return
    
    name = name_input.capitalize()
    
    email = simpledialog.askstring("Cadastrar Participante", f"E-mail para ID {p_id}:")
    if not email: return
    
    preferences = simpledialog.askstring("Cadastrar Participante", f"Preferências Temáticas para ID {p_id} (ex: IA, Web):")
    if not preferences: return
    
    # Armazena o participante no dicionário global de participantes
    data_manager.participants_data[p_id] = {"name": name, "email": email, "preferences": preferences}
    messagebox.showinfo("Sucesso", f"Participante '{name}' (ID: {p_id}) cadastrado.")
  