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
        p_id = p_id.upper()
        
    if p_id in data_manager.participants_data:
        messagebox.showerror("Erro',f'ID de participante '{p_id}' já existe.")
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
  
  
# -----------------------------------------------------------------
# Listar participantes de um evento
# -----------------------------------------------------------------
  
def list_participants_by_event():
    """
    Lista todos os participantes inscritos em um evento específico.

    Processo:
    1. Solicita o nome do evento (com verificação de entrada).
    2. Verifica se o evento existe.
    3. Se o evento não tem participantes, informa.
    4. Obtém a lista de IDs de participantes do evento e os ordena.
    5. Usa `map` para transformar cada ID de participante em uma string formatada
       com os detalhes do participante.
    6. Constrói e exibe a lista de participantes em uma nova janela.
    """
    
    event_name_input = simpledialog.askstring("Listar Participantes por Evento", "Digite o nome do evento:")
    if not event_name_input: # Verifica entrada
        return
    
    event_name = event_name_input.capitalize()
    
    event = data_manager.events_data.get(event_name)
    if not event:
        messagebox.showerror("Erro", "Evento não encontrado.")
        return
    
    if not event['participants']:
        messagebox.showinfo("Participantes do Evento", f"O evento '{event_name}' não possui participantes.")
        return
    
    # Ordena a lista de IDs de participantes para uma exibição organizada
    sorted_p_ids = sorted(event['participants'])
    
    # --- Usando map para formatar cada participante em uma string ---
    # map(funcao, iteravel) aplica 'funcao' a cada item do 'iteravel'.
    # Aqui, o iterável é a lista sorted_p_ids.
    # A função lambda pega cada p_id da lista e busca suas informações em data_manager.participants_data.
    # Em seguida, retorna uma string formatada para aquele participante.
    
#Operador Morsa (:=): Ele permite que você atribua um valor a uma variável E, ao mesmo tempo, use esse valor em uma expressão.
    
# and é "lazy" (preguiçoso). Ele avalia a expressão da esquerda primeiro.
# Se a expressão da esquerda for falsa None a expressão da direita não é avaliada, e o and retorna o valor da expressão da esquerda (que é None).

# Se a expressão da esquerda for verdadeira um dicionário preenchido,a expressão da direita é avaliada, 
# e o and retorna o valor da expressão da direita.
    
    
    formatted_participants = map(lambda p_id_in_event:
                                (p_info := data_manager.participants_data.get(p_id_in_event)    #Operador Morsa (:=) - Walrus Operator:
                                ) and ( 
                                    f"ID: {p_id_in_event}, Nome: {p_info['name']}, Email: {p_info['email']}"
                                    if p_info else # Se p_info existe, formata normalmente
                                    f"ID: {p_id_in_event}: (Dados do participante não encontrados - inconsistência)" # Se p_info é None
                                ), sorted_p_ids
                                 )
    
    # formatted_participants é um ITERADOR.

    # Junta todas as strings formatadas de participantes em uma única grande string.
    
    participants_str = f"--- Participantes do Evento: {event_name} (Ordenado por ID) ---\n\n" + "\n".join(formatted_participants) + "\n--------------------------------------"
    
    show_in_new_window(f"Participantes em {event_name}", participants_str)
    
    
    
    
    
# -----------------------------------------------------------------
# Pesquisar participante por ID
# -----------------------------------------------------------------

def search_participant_by_id():
    """
    Busca e exibe as informações de um participante específico pelo seu ID.

    Processo:
    1. Solicita o ID do participante (com verificação de entrada).
       - `.upper()`: Converte a entrada para maiúsculas para que a busca seja consistente.
    2. Verifica se o participante existe.
    3. Exibe os detalhes do participante em uma messagebox.
    """
    p_id_input = simpledialog.askstring("Buscar Participante por ID", "Digite o ID do participante:")
    if not p_id_input: # Verifica entrada
        return
    p_id = p_id_input.upper() # Converte para maiúsculas

    participant_info = data_manager.participants_data.get(p_id)
    if not participant_info:
        messagebox.showerror("Erro", "Participante não encontrado.")
        return
    
    info_str = f"--- Informações do Participante ---\n" \
               f"ID: {p_id}\n"\
               f"Nome: {participant_info['name']}\n"\
               f"Gmail: {participant_info['gmail']}\n"\
               f"Preferências: {participant_info['preferences']}\n"\
               f"------------------------------------"
               
#A barra invertida \ no final de uma linha em Python diz para o código continuar na linha de baixo. caractere de continuação de linha.
#\n, que é um caractere especial dentro de uma string que causa uma quebra de linha no texto exibido, não no código em si.





# -----------------------------------------------------------------
# Adiciionar partcippante e evento
# -----------------------------------------------------------------

def add_participant_to_event():
    """
    Inscreve um participante em um evento.

    Processo:
    1. Solicita o nome do evento e o ID do participante (com verificações de entrada).
    2. Verifica se o evento existe.
    3. **Verifica o Participante:** Se o participante não existe, pergunta se o usuário deseja cadastrá-lo.
       - Se sim, chama `add_new_participant_data()` (que pode gerar ID automático).
       - Se não, informa e cancela a operação.
    4. Verifica se o participante já está inscrito no evento para evitar duplicatas.
    5. Adiciona o ID do participante à lista de participantes do evento.
    6. Confirma a inscrição.
    """
    event_name_input = simpledialog.askstring("Adicionar Participante ao Evento", "Nome do Evento:")
    if not event_name_input: # Verifica entrada
        return
    event_name = event_name_input.capitalize() # Capitaliza o nome do evento

    if event_name not in data_manager.events_data:
        messagebox.showerror("Erro", "Evento não encontrado.")
        return
    
    p_id_input = simpledialog.askstring("Adicionar Participante ao Evento", "ID do Participante:")
    if not p_id_input: # Verifica entrada
        return
    p_id = p_id_input.upper() # Converte ID para maiúsculas
    
     # --- Se o participante não está no sistema, apenas informa e sai. ---
    if p_id not in data_manager.participants_data:
        messagebox.showerror("Erro", f"Participante com ID '{p_id}' não cadastrado no sistema. Por favor, cadastre-o primeiro.")
        return # Sai da função, não oferece mais opções.
    # --- Fim da Lógica Simplificada ---

    # Verifica se o participante já está na lista do evento
    if p_id in data_manager.events_data[event_name]['participants']:
        messagebox.showinfo("Informação", "Participante já está inscrito neste evento.")
        return

    data_manager.events_data[event_name]['participants'].append(p_id)
    messagebox.showinfo("Sucesso", f"Participante {p_id} adicionado ao evento '{event_name}'.")
    
    
    
# -----------------------------------------------------------------
#Remover partcippante de evento
# -----------------------------------------------------------------
def remove_participant_from_event():
    """
    Remove um participante de um evento específico.

    Processo:
    1. Solicita o nome do evento e o ID do participante (com verificações de entrada).
    2. Verifica se o evento existe.
    3. Verifica se o participante está inscrito naquele evento.
    4. Remove o ID do participante da lista de participantes do evento.
    5. Confirma a remoção.
    """
    event_name_input = simpledialog.askstring("Remover Participante do Evento", "Nome do Evento:")
    if not event_name_input: # Verifica entrada
        return
    event_name = event_name_input.capitalize() # Capitaliza o nome do evento
    
    if event_name not in data_manager.events_data:
        messagebox.showerror("Erro", "Evento não encontrado.")
        return
    
    p_id_input = simpledialog.askstring("Remover Participante do Evento", "ID do Participante a remover:")
    if not p_id_input: # Verifica entrada
        return
    p_id = p_id_input.upper() # Converte ID para maiúsculas