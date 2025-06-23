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
import datetime # Importamos o módulo datetime fornece classes e funções 
# para trabalhar com datas e horas.

# Importa as variáveis de dados e funções auxiliares de outros módulos
import data_manager
from gui_elements import show_in_new_window

# =================================================================
# Funções de Gerenciamento de Eventos
# =================================================================


# -----------------------------------------------------------------
# Exibir eventos
# -----------------------------------------------------------------
def display_events():
    """
    Exibe uma lista detalhada de todos os eventos cadastrados no sistema.

    Processo:
    1. Verifica se há eventos. Se não, informa o usuário.
    2. Usa `map` para transformar cada dicionário de evento em uma string formatada.
       Pense em: para cada 'figurinha de evento', crie um 'cartão de descrição'.
    3. Junta todos os 'cartões de descrição' em uma única string longa.
    4. Exibe esta string em uma nova janela de texto rolável.
    """
    
    if not data_manager.events_data: # Verifica se o dicionário de eventos está vazio
        messagebox.showinfo("Exibir Eventos", "Nenhum evento cadastrado.")
        return # Sai da função se não houver eventos
    
    # =================================================================
    # items() = É um método de dicionários que retorna uma lista de pares
    # (chave, valor). No nosso "álbum", ele te dá o nome da figurinha e a figurinha em si.
    
    # \n é um caractere especial que representa uma quebra de linha,
    # fazendo com que o próximo texto apareça na linha de baixo.
    # =================================================================
    
     # --- Usando map para formatar cada evento em uma string ---
    # map(funcao, iteravel) aplica 'funcao' a cada item do 'iteravel'.
    # Aqui, o iterável é data_manager.events_data.items(), que nos dá (name, details) para cada evento.
    # A função lambda é a "receita" de como formatar cada (item), par (name, details).
    # Ela retorna uma string formatada para cada evento.
    
    formatted_events = map(
        lambda item: (
            f"Nome: {item[0]}\n" # item[0] é o 'name' (chave do dicionário events_data)
            f"Data: {item[1]['data']}\n" # item[1] é o 'details' (valor do dicionário events_data), e acessamos a 'data' dentro dele
            f"Tema: {item[1]['theme']}\n"
            f"Participantes: {len(item[1]['participants'])}\n"
            f"------------------------" # Separador para cada evento, sem \n final aqui
        ),
        data_manager.events_data.items() #gera a tupla (chave, valor) --> item
    )
    # formatted_events é um ITERADOR, não uma lista. Ele vai gerar as strings sob demanda.

    # Junta todas as strings formatadas de eventos em uma única grande string.
    # '\n\n'.join(...) coloca duas quebras de linha entre cada bloco de evento.
    events_str = "--- Lista de Eventos ---\n\n" + "\n\n".join(formatted_events)
    
    show_in_new_window("Lista de Eventos", events_str) # Exibe o texto na nova janela
    
    
    
    
    
# -----------------------------------------------------------------
# Verificação de data
# -----------------------------------------------------------------

def is_valid_date(date_str):
    """
    Função auxiliar para validar se uma string corresponde a uma data válida no formato AAAA-MM-DD.

    Como funciona (Algoritmo de Validação de Data):
    1. Tenta converter a string `date_str` para um objeto de data usando `datetime.datetime.strptime()`.
       - `strptime()`: Significa "string parse time" (analisar string de tempo).
       - O primeiro argumento é a string que queremos validar.
       - O segundo argumento é o "formato esperado" (`%Y-%m-%d` significa Ano-4 dígitos, Mês-2 dígitos, Dia-2 dígitos, separados por hífens).
    
    2. Se a conversão for bem-sucedida, a string é uma data válida no formato esperado, e a função retorna True.
    
    3. Se a conversão falhar (por exemplo, se a data for "2023-02-30" que não existe, ou "abc", ou "2025/01/01" com formato errado), 
    um `ValueError` será levantado.
    
    4. O bloco `except ValueError:` captura esse erro, e a função retorna False, indicando que a data é inválida.
    """
    
    try:
        # Tenta criar um objeto de data a partir da string com o formato especificado.
        # Se a string não for uma data real ou não estiver no formato correto, isso irá falhar.
        datetime.datetime.strptime(date_str,'%Y-%m-%d')
        return True # Se chegou aqui, a conversão funcionou, então a data é válida.
    
    except ValueError:
        # Se um ValueError ocorrer, significa que a string não é uma data válida ou não está no formato esperado.
        return False # A data é inválida.
        
        
# -----------------------------------------------------------------
# Adicionar evento
# -----------------------------------------------------------------

def add_new_event():
    """
    Permite adicionar um novo evento ao sistema, solicitando Nome, Data e Tema.

    Processo:
    1. Solicita o nome do evento ao usuário.
       - `.capitalize()`: Garante que a primeira letra seja maiúscula e o restante minúscula,
                         para padronizar os nomes de eventos no sistema.
    
    2. Verifica se o nome foi fornecido e se já não existe um evento com o mesmo nome.
    
    3. **LOOP DE VALIDAÇÃO DE DATA:** Solicita a data repetidamente até que uma data válida seja fornecida.
       - `.capitalize()` para o tema: Padroniza também o tema.
    
    4. Solicita o tema e o capitaliza.
    
    5. Adiciona o novo evento ao dicionário `events_data` com uma lista vazia de participantes.
    
    6. Confirma a adição com uma mensagem.
    
    =================================================================
    
    simpledialog.askstring(...): é uma função do Tkinter que abre uma pequena janela de diálogo 
    pop-up projetada especificamente para receber uma string (texto) como entrada do usuário.
    """
    
    name_input = simpledialog.askstring("Adicionar Evento", "Nome do Evento:") #caixinha que pergunta o nome
    if not name_input: # se n tiver nada escrito sai da função
        return
    
    name = name_input.capitalize()
    
    if name in data_manager.events_data: # se o mesmo nome no events_data ele sai da função 
        messagebox.showerror("Erro", "Evento com este nome já existe.")
        return
        
        # --- INÍCIO DA VALIDAÇÃO DE DATA ---
    # Usamos um loop 'while True' para continuar pedindo a data
    # até que uma data válida seja inserida ou o usuário cancele.
    
    while True:
        data = simpledialog.askstring("Adicionar Evento", "Data (AAAA-MM-DD):")
        
        if not data: # Se o usuário cancelar (retorna None) ou digitar vazio (retorna "")
            # Sai do loop e da função add_new_event se o usuário não quiser fornecer a data.
            return 
        
        # Chama a nossa função auxiliar is_valid_date para verificar a data.
        if is_valid_date(data):
            # Se a data for válida, sai do loop 'while True'.
            break 
        else:
            # Se a data for inválida, informa o usuário e o loop continua para pedir a data novamente.
            messagebox.showerror("Erro de Data", "Formato de data inválido ou data inexistente. Por favor, use o formato AAAA-MM-DD (ex: 2025-07-10).")
    
    # --- FIM DA VALIDAÇÃO DE DATA ---
    
    theme_input = simpledialog.askstring("Adicionar Evento", "Tema Central:")
    if not theme_input: return
    
    theme = theme_input.capitalize()
    
    # Aplica .capitalize() SOMENTE se a entrada for válida: Se a execução passar pelo if not theme: return
    # Adiciona o evento ao dicionário, com a data validada e o tema capitalizado
    data_manager.events_data[name] = {"data": data, "theme": theme, "participants": []}
    messagebox.showinfo("Sucesso", f"Evento '{name}' adicionado.")
    
    
    
# -----------------------------------------------------------------
# Remover evento
# -----------------------------------------------------------------

def remove_event():
    """
    Permite remover um evento existente do sistema, solicitando o nome.

    Processo:
    1. Solicita o nome do evento a ser removido.
       - `.capitalize()`: Para que a busca seja consistente com a forma que os nomes são armazenados.
       
    2. Verifica se o evento existe.
    
    3. Remove o evento do dicionário `events_data` usando `del`.
    
    4. Confirma a remoção.
    
    
    del: remove permanentemente o par chave-valor (name e todos os detalhes do evento associados a ele) 
    do dicionário data_manager.events_data.
    """
    
    name_input = simpledialog.askstring("Remover Evento", "Nome do Evento a remover:")
    if not name_input: return
    
    name = name_input.capitalize()
    
    if name in data_manager.events_data:
        del data_manager.events_data[name] # Remove a entrada do dicionário
        messagebox.showinfo("Sucesso", f"Evento '{name}' removido.")
    else:
        messagebox.showerror("Erro", "Evento não encontrado.")
        
        
        

# -----------------------------------------------------------------
# Atualiza evento
# -----------------------------------------------------------------


def update_event_info():
    """
    Permite atualizar informações específicas de um evento existente (nome, data ou tema).

    Processo:
    1. Solicita o nome do evento a ser atualizado.
   
    2. Verifica se o evento existe.
   
    3. Pergunta qual campo o usuário deseja atualizar ("nome", "data" ou "tema").
   
    4. Solicita o novo valor.
   
    5. Se for o nome, realiza uma operação especial para mudar a chave do dicionário.
   
    6. Se for data ou tema, atualiza o valor correspondente.
   
    7. Confirma a atualização.
    
    
    
    data_manager.events_data[event_name] pra acessar o valor se n existir da erro do tipo KeyError (erro de chave), e seu programa travaria.
    
    Usando o método .get(): data_manager.events_data.get(event_name): e a event_name não existir no dicionário, em vez de levantar um KeyError, 
    o método .get() simplesmente retorna o valor None (que significa "nada").
    
    event_name é a chave principal que você está buscando (por exemplo, "Workshop de IA").
        - O método .get() procura por essa event_name no dicionário data_manager.events_data. 
        - Se ele encontra a chave, ele retorna o valor completo associado a essa chave. 
    """
    
    event_name_input = simpledialog.askstring("Atualizar Evento", "Nome do Evento a atualizar:")
    if not event_name_input: return
    
    event_name = event_name_input.capitalize()

    # Usando .get() para analisar as key principais e obter o dicionário de detalhes do evento dentro delas.
    # 'event_details' agora é uma referência direta ao dicionário interno do evento.
    event_details = data_manager.events_data.get(event_name) # .get() retorna None se a chave não existe
    if not event_details:
        messagebox.showerror("Erro", "Evento não encontrado.")
        return
    
    # Aumentamos as opções para incluir "nome"
    borboleta_input = simpledialog.askstring("Atualizar Evento", "Campo para atualizar (nome, data, tema):")
    if not borboleta_input: return
        
    borboleta = borboleta_input.lower()
        
        
    # --- Lógica de atualização de campo ---
    if borboleta == "nome":
        # === CASO ESPECIAL: ATUALIZAR O NOME DO EVENTO (que é a CHAVE) ===
        new_name_input = simpledialog.askstring("Atualizar Evento", "Novo nome para o evento:")
        if not new_name_input:
            messagebox.showerror("Erro", "Novo nome inválido. Atualização cancelada.")
            return
        
        new_name = new_name_input.capitalize()
        
        if new_name == event_name:
            messagebox.showinfo("Informação", "O novo nome é o mesmo que o atual. Nenhuma alteração feita.")
            return

        if new_name in data_manager.events_data:
            messagebox.showerror("Erro", f"Já existe um evento com o nome '{new_name}'.")
            return
        
        # 1. Armazena os detalhes do evento atual antes de deletar
        # Precisamos de uma cópia dos detalhes, ou o 'del' abaixo os removerá.
        # Mas 'event_details' já é uma referência ao objeto, então vamos manipulá-lo e depois reatribuir.
        
        # 2. Deleta a entrada antiga do dicionário usando o nome antigo como chave
        del data_manager.events_data[event_name]
        
        # 3. Adiciona uma nova entrada ao dicionário com o novo nome como chave
        # Os 'event_details' ainda contêm os mesmos dados (data, theme, participants).
        # Apenas a chave externa no dicionário principal muda.
        data_manager.events_data[new_name] = event_details
        
        messagebox.showinfo("Sucesso", f"Nome do evento '{event_name}' atualizado para '{new_name}'.")
        
        
        
        
        
    elif borboleta == "data":
        # === ATUALIZAR A DATA ===
        while True: # Loop de validação de data
            new_date = simpledialog.askstring("Atualizar Evento", "Nova data (AAAA-MM-DD):")
            if not new_date:
                messagebox.showerror("Erro", "Valor inválido. Atualização cancelada.")
                return # Sai da função se o usuário cancelar
            
            if is_valid_date(new_date):
                event_details['data'] = new_date # Atualiza a data no dicionário de detalhes
                messagebox.showinfo("Sucesso", f"Data do evento '{event_name}' atualizada para '{new_date}'.")
                break # Sai do loop de validação
            else:
                messagebox.showerror("Erro de Data", "Formato de data inválido ou data inexistente. Por favor, use o formato AAAA-MM-DD (ex: 2025-07-10).")
    
    
    
    
    elif borboleta == "theme":
        # === ATUALIZAR O TEMA ===
        new_theme_input = simpledialog.askstring("Atualizar Evento", "Novo tema:")
        if not new_theme_input:
            messagebox.showerror("Erro", "Valor inválido. Atualização cancelada.")
            return
        
        new_theme = new_theme_input.capitalize()
        
        event_details['theme'] = new_theme # Capitaliza e atualiza o tema
        messagebox.showinfo("Sucesso", f"Tema do evento '{event_name}' atualizado para '{event_details['theme']}'.")
    
    else:
        # === CAMPO INVÁLIDO ===
        messagebox.showerror("Erro", "Campo inválido para atualização. Escolha 'nome', 'data' ou 'tema'.")



    