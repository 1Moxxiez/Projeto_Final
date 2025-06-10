# minha_casa.py

import tkinter as tk # Importa a biblioteca Tkinter

# Esta variável _minha_porta_principal é como um "registro" interno.
# Ela vai guardar a referência da porta principal da casa.
_minha_porta_principal = None 

def set_porta_principal(porta):
    """
    Esta função é a que você usa para "registrar" a porta principal da sua casa.
    Ela recebe a porta (a janela principal) e a guarda na nossa variável interna.
    """
    global _minha_porta_principal # Dizemos que vamos modificar a variável global
    _minha_porta_principal = porta
    print(f"DEBUG: Porta principal registrada como: {_minha_porta_principal}")

def instalar_janelinha_extra(titulo):
    """
    Esta função tenta instalar uma janelinha extra (pop-up).
    Para fazer isso, ela PRECISA saber qual é a porta principal da casa.
    """
    if _minha_porta_principal is None:
        print("ERRO: Não consigo instalar a janelinha! Ninguém me disse qual é a porta principal da casa!")
        return

    # Se a porta principal foi registrada, podemos instalar a janelinha nela
    janelinha = tk.Toplevel(_minha_porta_principal) # A janelinha é "filha" da porta principal
    janelinha.title(titulo)
    tk.Label(janelinha, text=f"Sou a {titulo}, instalada na sua casa!").pack()
    print(f"DEBUG: Janelinha '{titulo}' instalada com sucesso.")