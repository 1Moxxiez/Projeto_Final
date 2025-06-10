import tkinter as tk

# 1. Cria a janela principal (sua "vitrine")
root = tk.Tk()
root.title("Minha Vitrine de Loja")
root.geometry("400x300") # Define o tamanho inicial da vitrine

# 2. Cria o primeiro Frame (sua "bandeja de produtos eletrônicos")
# Este frame será cinza claro e terá um espaçamento interno de 10 pixels.
frame_eletronicos = tk.Frame(root, bg="lightgray", padx=10, pady=10)

# 3. Coloca alguns "produtos" (Labels) dentro do frame de eletrônicos
label_tv = tk.Label(frame_eletronicos, text="Smart TV 55\"", bg="lightgray")
label_tv.pack(pady=5) # Adiciona a TV na bandeja, com espaço vertical

label_celular = tk.Label(frame_eletronicos, text="Smartphone X", bg="lightgray")
label_celular.pack(pady=5) # Adiciona o celular na bandeja

# 4. Posiciona o frame_eletronicos na janela principal
# pack() organiza em blocos. Sem opções, ele fica no topo por padrão.
# expand=True e fill="x" faz com que o frame preencha horizontalmente.
frame_eletronicos.pack(pady=20, fill="x", expand=True)


# 5. Cria o segundo Frame (sua "prateleira de livros")
# Este frame será marrom claro e também terá um espaçamento interno.
frame_livros = tk.Frame(root, bg="tan", padx=10, pady=10)


# 6. Coloca alguns "produtos" (Labels) dentro do frame de livros
label_romance = tk.Label(frame_livros, text="Livro de Romance", bg="tan")
label_romance.pack(pady=5)

label_ficcao = tk.Label(frame_livros, text="Livro de Ficção Científica", bg="tan")
label_ficcao.pack(pady=5)

# 7. Posiciona o frame_livros na janela principal
# Ele será colocado abaixo do frame_eletronicos.
# fill="x" o faz preencher horizontalmente.
frame_livros.pack(pady=10, fill="x")


# 8. Inicia o loop principal da Tkinter para manter a janela aberta
root.mainloop()