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
# Adicionar evento
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
    
    name = simpledialog.askstring("Adicionar Evento", "Nome do Evento:").capitalize() #caixinha que pergunta o nome
    if not name: # se n tiver nada escrito sai da função
        return
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
    
    theme = simpledialog.askstring("Adicionar Evento", "Tema Central:")
    if not theme: return
    
    # Aplica .capitalize() SOMENTE se a entrada for válida: Se a execução passar pelo if not theme: return
    # Adiciona o evento ao dicionário, com a data validada e o tema capitalizado
    data_manager.events_data[name] = {"data": data, "theme": theme.capitalize(), "participants": []}
    messagebox.showinfo("Sucesso", f"Evento '{name}' adicionado.")