#

import tkinter as tk
from tkinter import scrolledtext # Precisamos importar scrolledtext para usá-lo

# Esta variável vai guardar a nossa "mesa de trabalho principal" (a janela 'root').
# Lembre-se, ela precisa ser definida pelo seu programa principal.
_mesa_de_trabalho_principal = None

def definir_mesa_principal(mesa):
    """
    Função para "avisar" a este módulo qual é a nossa mesa de trabalho principal.
    """
    global _mesa_de_trabalho_principal
    _mesa_de_trabalho_principal = mesa
    print("DEBUG: Mesa de trabalho principal definida.")

def show_in_new_window(title, content):
    """
    Função para abrir uma "folha de papel separada" (janela pop-up)
    e escrever um relatório nela.
    """
    # Checa se a "mesa de trabalho principal" foi definida.
    # Se não foi, não tem onde "colar" a nova folha de papel.
    if _mesa_de_trabalho_principal is None:
        print("ERRO: A mesa de trabalho principal não foi definida. Não consigo criar a janela!")
        return

    # 1. tk.Toplevel(_mesa_de_trabalho_principal):
    #    Cria a "folha de papel separada". O (_mesa_de_trabalho_principal)
    #    diz: "Essa folha pertence àquela mesa ali".
    nova_folha = tk.Toplevel(_mesa_de_trabalho_principal) 
    print(f"DEBUG: Criada nova folha de papel (Toplevel) com título: {title}")

    # 2. new_window.title(title):
    #    Dá um título para a sua folha de papel (aparece na barra superior da janela).
    nova_folha.title(title) 

    # 3. scrolledtext.ScrolledText(...):
    #    Cria a "área para escrever o relatório", que já vem com o mecanismo de rolagem.
    #    - wrap=tk.WORD: Se o texto for muito longo, ele quebra a linha na palavra,
    #      para não cortar as palavras no meio.
    #    - width=80, height=25: Define o tamanho inicial da área de escrita (em caracteres).
    area_de_relatorio = scrolledtext.ScrolledText(nova_folha, wrap=tk.WORD, width=80, height=25)
    print("DEBUG: Criada área de relatório com rolagem.")

    # 4. text_area.pack(padx=10, pady=10):
    #    "Cola" a área de relatório na sua "folha de papel separada".
    #    - padx/pady: Adiciona um espacinho nas bordas, para não ficar colado.
    area_de_relatorio.pack(padx=10, pady=10) 
    print("DEBUG: Área de relatório empacotada na janela.")

    # 5. text_area.insert(tk.END, content):
    #    Escreve o relatório real (o 'content' que você passou) na área de relatório.
    #    - tk.END: Coloca o texto no final do que já estiver escrito (útil se você for adicionar mais tarde).
    area_de_relatorio.insert(tk.END, content) 
    print("DEBUG: Conteúdo inserido na área de relatório.")

    # 6. text_area.config(state=tk.DISABLED):
    #    Torna a área de relatório "somente leitura".
    #    Você não quer que as pessoas rabisquem seu relatório, certo?
    area_de_relatorio.config(state=tk.DISABLED) 
    print("DEBUG: Área de relatório definida como somente leitura.")