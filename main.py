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
import gui_elements       # Funções de interface (como nova janela de texto)
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
gui_elements.set_root_window(root)





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
main_frame = tk.Frame(root, padx=20, pady=20) # Adiciona padding interno ao frame
main_frame.pack(expand=True, fill='both')




# -----------------------------------------------------------------
# 3. Títulos e Descrição na Janela Principal
# -----------------------------------------------------------------

'''
 `Label` é um widget para exibir texto ou imagens.
 Coloca alguns "itens" (Labels) dentro do main_frame
 
 \n é um caractere de quebra de linha
 wraplength: define a largura máxima em pixels antes que o texto seja automaticamente quebrado para a próxima linha

'''

title_label = tk.Label(main_frame, text='Gerenciamento de Eventos',
                       font=('Arial', 28, 'bold'), fg= "#000000")
                                           #bold = negrito, tipo de letra maior 
                                        
 # `pady` adiciona espaçamento vertical abaixo do label.
title_label.pack(padx=(10, 20)) #terá 10 pixels de espaço acima dele e 20 pixels de espaço abaixo dele  

description_label = tk.Label(main_frame,  
                             text="Bem-vindo ao Sistema de Gerenciamento de Eventos da Comunidade Tech.\n"
                                  "Use os botões abaixo ou o menu superior para interagir com o sistema.",
                                  font=("Arial", 14), wraplength=800, justify=tk.CENTER, fg="#000000")  


description_label.pack(pady=10)





# -----------------------------------------------------------------
# 4. Botões de Ações Comuns na Janela Principal
# -----------------------------------------------------------------

'''

Criando botões para as funcionalidades mais acessadas.
 `tk.Button(...)` cria um botão.
 `text`: O texto exibido no botão.
 `command`: A função Python que será chamada quando o botão for clicado.
            É importante não colocar parênteses na função (ex: `adicionar()` está errado, `adicionar` é o certo),
            porque queremos passar a referência da função, não o resultado de sua execução.
 `font`: Define a fonte e tamanho do texto do botão.
 `width`, `height`: Define o tamanho do botão em unidades de texto.
 `bg`, `fg`: Cor de fundo e cor do texto (background/foreground).
 `activebackground`: Cor de fundo quando o botão está sendo clicado.
 `grid()`: É outro gerenciador de layout. Ele organiza os widgets em uma grade (linhas e colunas).
           - `row`: A linha na grade.
           - `column`: A coluna na grade.
           - `padx`, `pady`: Espaçamento externo horizontal e vertical entre os botões.


'''

# Outro Frame para agrupar os botões, melhorando a organização do layout.
button_frame = tk.Frame(main_frame, pady=20, bg="#BABFC5")
button_frame.pack()



# Botões de Eventos
description_button = tk.Label(button_frame,text='Eventos',
                       font=('Arial', 12, 'bold'), fg= "#000000", bg="#BABFC5").grid(row=0, column=0, )

tk.Button(button_frame, text='Adicionar Evento', command= ..., 
          font=('Arial', 12), width=25, height=2, bg="#6C0D95", fg="white", activebackground='#8613B7').grid(row=1, column=0, padx=10, pady=2)
tk.Button(button_frame, text="Exibir Eventos", command=..., 
          font=("Arial", 12), width=25, height=2, bg="#6C0D95", fg="white", activebackground="#8613B7").grid(row=2, column=0, padx=10, pady=5)
tk.Button(button_frame, text="Remover Evento", command=..., 
          font=("Arial", 12), width=25, height=2, bg="#6C0D95", fg="white", activebackground="#8613B7").grid(row=3, column=0, padx=10, pady=5)


# Botões de Participantes
description_button = tk.Label(button_frame,text='Participantes',
                       font=('Arial', 12, 'bold'), fg= "#000000", bg="#BABFC5").grid(row=0, column=1, padx=10, pady=2)

tk.Button(button_frame, text="Cadastrar Novo Participante", command=...,
          font=("Arial", 12), width=25, height=2, bg="#15718A", fg="white", activebackground="#0097a7").grid(row=1, column=1, padx=10, pady=5)
tk.Button(button_frame, text="Listar Todos os Participantes", command=...,
          font=("Arial", 12), width=25, height=2, bg="#15718A", fg="white", activebackground="#0097a7").grid(row=2, column=1, padx=10, pady=5)
tk.Button(button_frame, text="Inscrever Participante em Evento", command=..., 
          font=("Arial", 12), width=25, height=2, bg="#15718A", fg="white", activebackground="#0097a7").grid(row=3, column=1, padx=10, pady=5)


# Outras Ações Chave (Estatísticas e Remoção Geral de Participante)
description_button = tk.Label(button_frame,text='Outros',
                       font=('Arial', 12, 'bold'), fg= "#000000", bg="#BABFC5").grid(row=0, column=2, padx=10, pady=2)

tk.Button(button_frame, text="Gerar Estatísticas", command=..., 
          font=("Arial", 12), width=25, height=2, bg="#BE1850", fg="white", activebackground="#E91E63").grid(row=1, column=2, padx=10, pady=5)
tk.Button(button_frame, text="Remover Participante (Geral)", command=...,
          font=("Arial", 12), width=25, height=2, bg="#BE1850", fg="white", activebackground="#E91E63").grid(row=2, column=2, padx=10, pady=5)
tk.Button(button_frame, text="Buscar Participante por ID", command=..., 
          font=("Arial", 12), width=25, height=2, bg="#BE1850", fg="white", activebackground="#E91E63").grid(row=3, column=2, padx=10, pady=5)




# -----------------------------------------------------------------
# 5. Barra de Menu Superior (Menubar)
# -----------------------------------------------------------------

# Cria a barra de menu que aparece no topo da janela.
menubar = tk.Menu(root)
root.config(menu=menubar) # Associa a barra de menu à janela principal




# Menu "Arquivo"
file_menu = tk.Menu(menubar, tearoff=0) # `tearoff=0` impede que o menu seja "arrancado" da barra
menubar.add_cascade(label="Arquivo", menu=file_menu) # Adiciona o menu "Arquivo" à barra de menu
# Adiciona itens ao menu "Arquivo"

file_menu.add_command(label="Importar Dados (Exemplo)", command=...)
file_menu.add_separator() # Adiciona uma linha separadora
file_menu.add_command(label="Sair", command=root.quit) # `root.quit` fecha a aplicação

# Menu "Eventos"
event_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Eventos", menu=event_menu)

event_menu.add_command(label="Exibir Todos os Eventos", command=...)
event_menu.add_command(label="Adicionar Novo Evento", command=...)
event_menu.add_command(label="Remover Evento", command=...)
event_menu.add_command(label="Atualizar Informações do Evento", command=...)
event_menu.add_separator()
event_menu.add_command(label="Identificar Eventos com Poucos Participantes", command=...)
event_menu.add_command(label="Agrupar Eventos por Tema", command=...) # Funções de relatório aqui
event_menu.add_command(label="Contar Eventos por Tema", command=...)

# Menu 'Participantes'
participant_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Participantes', menu=participant_menu)

participant_menu.add_command(label="Cadastrar Novo Participante (ID Automático)", command=...)
participant_menu.add_command(label="Listar Todos os Participantes (Ordenado por ID)", command=...)
participant_menu.add_command(label="Listar Participantes por Evento", command=...)
participant_menu.add_command(label="Buscar Participante por ID", command=...)
participant_menu.add_command(label="Inscrever Participante em Evento", command=...)
participant_menu.add_command(label="Remover Participante de Evento", command=...)
participant_menu.add_command(label="Remover Participante Completamente do Sistema", command=...)
participant_menu.add_command(label="Atualizar Informações do Participante", command=...)
participant_menu.add_separator()
participant_menu.add_command(label="Detectar e Remover Duplicatas em Eventos", command=...)
participant_menu.add_command(label="Listar Eventos por Participante", command=...)


# Menu "Relatórios e Estatísticas"
reports_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Relatórios e Estatísticas", menu=reports_menu)
reports_menu.add_command(label="Gerar Estatísticas Gerais", command=...)
reports_menu.add_command(label="Calcular Taxa Média de Participação por Tema", command=...)

# Menu "Busca"
search_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Busca", menu=search_menu)
search_menu.add_command(label="Busca Filtrada (Tema/Data)", command=...)


# -----------------------------------------------------------------
# 6. Iniciar o Loop Principal da Aplicação
# -----------------------------------------------------------------

# `root.mainloop()`: Esta linha é a mais importante para iniciar a GUI.
# Ela inicia o "loop de eventos" do Tkinter. A aplicação fica rodando,
# esperando por interações do usuário (cliques em botões, digitação, etc.).
# Sem esta linha, a janela Tkinter apareceria e fecharia imediatamente.
root.mainloop()