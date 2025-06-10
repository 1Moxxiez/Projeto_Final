# 

import tkinter as tk
import minhas_janelas_auxiliares # Importa o nosso módulo

# 1. Cria a "mesa de trabalho principal" (janela principal)
mesa_principal = tk.Tk()
mesa_principal.title("Minha Mesa de Trabalho Principal")
mesa_principal.geometry("500x300")

# 2. **AVISA** ao módulo minhas_janelas_auxiliares qual é a mesa principal.
# Essa é a linha que você está perguntando: "aqui, essa é a minha mesa!"
minhas_janelas_auxiliares.definir_mesa_principal(mesa_principal)

# 3. Agora, vamos criar um botão na mesa principal para gerar um relatório
def gerar_relatorio_exemplo():
    titulo_relatorio = "Relatório de Vendas do Mês"
    conteudo_relatorio = """
    Relatório de Vendas - Junho 2025

    - Produto A: 150 unidades
    - Produto B: 230 unidades
    - Produto C: 80 unidades
    - Serviço X: 45 vendas
    - Serviço Y: 12 vendas

    Observações:
    As vendas do Produto B superaram as expectativas.
    O Serviço Y teve uma queda em relação ao mês anterior,
    precisamos investigar as causas.
    A equipe de marketing deve focar em promoções para o Produto C.

    Este é um relatório de exemplo para demonstrar a funcionalidade
    da janela de exibição de conteúdo longo. Se o texto for ainda
    mais longo, a barra de rolagem aparecerá automaticamente,
    permitindo que você leia todo o conteúdo.
    """
    # Chamamos a função do nosso módulo auxiliar para mostrar o relatório
    minhas_janelas_auxiliares.show_in_new_window(titulo_relatorio, conteudo_relatorio)

tk.Button(mesa_principal, text="Ver Relatório Detalhado", command=gerar_relatorio_exemplo).pack(pady=50)

# 4. Inicia o loop principal da Tkinter
mesa_principal.mainloop()