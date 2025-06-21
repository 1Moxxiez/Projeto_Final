'''
Conterá funções auxiliares para a interface gráfica (como exibir janelas de texto).
'''

# =================================================================
# MÓDULO: ELEMENTOS DA INTERFACE GRÁFICA (GUI ELEMENTS)
#

#
# Conceitos Chave:
# - Tkinter: Biblioteca padrão do Python para criar GUIs.
# - Toplevel: Uma nova janela independente da janela principal.
# - ScrolledText: Um widget de texto que inclui barras de rolagem
#                 automaticamente, útil para exibir muito texto.
# =================================================================

import tkinter as tk
from tkinter import scrolledtext

# A variável `root` representa a janela principal da sua aplicação Tkinter.
# É importante que ela seja definida em `main.py` e seja acessível aqui,
# pois novas janelas (Toplevel) precisam de uma janela "pai".
# Vou imagina que `root` é globalmente acessível após inicialização.

_root_window = None # Será definida pela função `set_root_window`


def set_root_window(root_window):
    """
    Define a janela raiz (root window) da aplicação.
    Esta função deve ser chamada UMA VEZ no início do seu programa principal (main.py)
    para que as janelas secundárias (Toplevel) saibam qual é a janela principal.
  
    Esta função é a que você usa para "registrar" a porta principal da sua casa.
    Ela recebe a porta (a janela principal) e a guarda na nossa variável interna.
    """
    
    global _root_window # Dizemos que vamos modificar a variável global
    _root_window = root_window
    

def show_in_new_window(title, content):
    """
    Cria uma nova janela Toplevel (janela pop-up) para exibir conteúdo de texto.

    Objetivo: Mostrar informações detalhadas (como listas de eventos, participantes, estatísticas)
              sem sobrecarregar a janela principal ou usar muitos messageboxes.

    Como Funciona:
    1. `tk.Toplevel(_root_window)`: Cria uma nova janela. `_root_window` é a janela "pai"
       (normalmente a janela principal do seu app). Isso garante que a nova janela
       seja tratada como parte da sua aplicação.
       
    2. `new_window.title(title)`: Define o título da nova janela.
    
    3. `scrolledtext.ScrolledText(...)`: Cria uma área de texto que automaticamente
       adiciona barras de rolagem se o conteúdo for muito grande.
    
       - `wrap=tk.WORD`: Garante que as linhas de texto quebrem em palavras inteiras,
         melhorando a legibilidade.
         
       - `width` e `height`: Definem o tamanho inicial da área de texto em caracteres.
    
    4. `text_area.pack(padx=10, pady=10)`: Posiciona a área de texto na nova janela.
       - `padx` e `pady`: Adicionam um espaçamento ao redor do texto.
    
    5. `text_area.insert(tk.END, content)`: Insere o texto `content` (o novo texto) no final (`tk.END` é como a última linha escrita do seu caderno)
       da área de texto.
    
    6. `text_area.config(state=tk.DISABLED)`: Torna a área de texto "somente leitura".
       Isso impede que o usuário digite ou altere o conteúdo, pois é apenas para exibição.

    Lembrete: Pense nela como um "caderninho" onde você anota e exibe relatórios longos.
    """
    
    if _root_window is None:
        # Se o root_window não foi definido, exibe uma mensagem de erro no console
        # e não tenta criar a janela. ajuda a depurar.
        print ("Erro: Janela raiz (root window) não definida em gui_elements.py. Chame set_root_window(root).")
        return
    
    new_window = tk.Toplevel(_root_window) #Cria uma nova janela pop-up, filha da janela principal
    new_window.title(title) #Define o título da nova janela
    
     # Cria uma área de texto com barras de rolagem automáticas
    text_area = scrolledtext.ScrolledText(new_window, wrap=tk.WORD, width=80, heigth=25)
    text_area.pack(padx=10,pady=10) # Posiciona a área de texto na janela
    text_area.insert(tk.END, content)# Insere o conteúdo fornecido no inicio da pagina
    text_area.config(state=tk.DISABLED)# Torna a área de texto somente leitura