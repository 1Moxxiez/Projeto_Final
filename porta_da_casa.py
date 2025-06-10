# faz_tudo.py

import tkinter as tk
import minha_casa # Importa o nosso módulo "minha_casa"

# 1. Criar a porta principal da casa (a janela principal)
porta_principal = tk.Tk()
porta_principal.title("Minha Casa Principal")
porta_principal.geometry("300x200")

# 2. **Aqui está a linha que você não entendeu!**
# Estamos "avisando" ao módulo 'minha_casa' qual é a nossa 'porta_principal'.
# É o mesmo que dizer: "minha_casa, guarda essa 'porta_principal' aí, é a sua referência!"
minha_casa.set_porta_principal(porta_principal)

# 3. Agora podemos pedir para instalar janelinhas extras
# Como 'minha_casa' já sabe qual é a porta principal, ele consegue instalar.
tk.Button(porta_principal, text="Instalar Janelinha 1", 
          command=lambda: minha_casa.instalar_janelinha_extra("Janelinha do Quarto")).pack(pady=10)

tk.Button(porta_principal, text="Instalar Janelinha 2", 
          command=lambda: minha_casa.instalar_janelinha_extra("Janelinha da Cozinha")).pack()

# 4. Iniciar o loop principal da Tkinter para manter a janela aberta
porta_principal.mainloop()