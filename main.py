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
# import data_manager       # Gerencia os dados
# import gui_elements       # Funções de interface (como nova janela de texto)
# import event_functions    # Funções para eventos
# import participant_functions # Funções para participantes
# import report_functions   # Funções para relatórios e estatísticas


# -----------------------------------------------------------------
# 1. Configuração da Janela Principal (Root Window)
# -----------------------------------------------------------------

# Cria a janela principal da aplicação Tkinter.
# `Tk()` é a classe que representa a janela raiz de uma aplicação GUI.

root = tk.Tk()  #root (que significa "raiz" em inglês) é o nome padrão dado à janela principal
root.title('Sistema de Gerenciamento de Eventos da Comunidade Tech') # Define o título da janela
root.geometry('900x650') # Define o tamanho inicial da janela (largura x altura em pixels)


# Informa ao módulo `gui_elements` qual é a janela raiz.
# Isso é crucial para que `show_in_new_window` possa criar janelas filhas corretamente.
# gui_elements.set_rot_window(root)





# -----------------------------------------------------------------
# 2. Frame Principal para Organização (Main Frame)
# -----------------------------------------------------------------


'''
 Um `Frame` é uma prateleira (widget contêiner) que pode agrupar outros objetos (label) widget.
 Usamos `main_frame` para organizar melhor os elementos dentro da janela `root`.

`pack()` é um gerenciador de layout que organiza widgets em blocos antes de colocá-los
na janela. 

`expand=True : faz o frame expandir com a janela
`fill="both" : o faz preencher tanto na horizontal quanto na vertical.
'''
main_frame = tk.Frame(root, padx=20, pady=20, bg="lightgray") # Adiciona padding interno ao frame
main_frame.pack(expand=True, fill='both')

# `root.mainloop()`: Esta linha é a mais importante para iniciar a GUI.
# Ela inicia o "loop de eventos" do Tkinter. A aplicação fica rodando,
# esperando por interações do usuário (cliques em botões, digitação, etc.).
# Sem esta linha, a janela Tkinter apareceria e fecharia imediatamente.
root.mainloop()




# -----------------------------------------------------------------
# 3. Títulos e Descrição na Janela Principal
# -----------------------------------------------------------------