# Sistema de Gerenciamento de Eventos da Comunidade Tech

Este é um sistema de linha de comando com interface gráfica simples, desenvolvido em Python usando Tkinter, para gerenciar eventos, participantes e gerar relatórios administrativos para a "Comunidade Tech".

=======================
## 🚀 Funcionalidades
=======================

O sistema oferece as seguintes funcionalidades, acessíveis tanto por botões na tela principal quanto por um menu superior:

### Gerenciamento de Eventos
* **Exibir Todos os Eventos**: Lista detalhada de todos os eventos cadastrados.
* **Adicionar Novo Evento**: Permite cadastrar um novo evento com nome, data e tema. Inclui validação para datas inválidas.
* **Remover Evento**: Exclui um evento existente do sistema.
* **Atualizar Informações do Evento**: Permite modificar o nome, a data ou o tema de um evento.
* **Identificar Eventos com Poucos Participantes**: Lista eventos com menos de dois participantes, sugerindo possíveis cancelamentos.

### Gerenciamento de Participantes
* **Cadastrar Novo Participante**: Adiciona um novo participante ao sistema, gerando um ID único e sequencial automaticamente (ex: P001, P002).
* **Listar Todos os Participantes**: Exibe uma lista de todos os participantes cadastrados, ordenados por ID.
* **Inscrever Participante em Evento**: Permite adicionar um participante existente a um evento específico.
* **Remover Participante de Evento**: Desvincula um participante de um evento específico.
* **Remover Participante Completamente do Sistema**: Exclui um participante de todos os eventos e do cadastro geral.
* **Buscar Participante por ID**: Exibe os detalhes de um participante específico.

### Relatórios e Estatísticas
* **Gerar Estatísticas Gerais**: Apresenta dados como o total de eventos, total de participantes, top 5 participantes mais ativos e temas mais frequentes.
* **Calcular Taxa Média de Participação por Tema**: Mostra a média de participantes por evento para cada tema.

### Busca
* **Buscar Evento por Nome**: Realiza uma busca simples por um evento específico utilizando seu nome.

===============================================
## ✨ Destaques Técnicos e Conceitos Aplicados
===============================================


* **Organização Modular**: Código dividido em múltiplos arquivos (`main.py`, `data_manager.py`, `event_functions.py`, `participant_functions.py`, `report_functions.py`, `gui_elements.py`) para melhor organização e reutilização.
* **Estruturas de Dados**: Utilização de dicionários para armazenar e acessar eventos e participantes por chaves únicas (nomes de eventos, IDs de participantes). Listas para gerenciar participantes em eventos.
* **Geração de IDs Sequenciais**: Algoritmo para gerar IDs de participantes automaticamente e em ordem crescente (ex: P001, P002).
* **Validação de Entrada**: Verificação e formatação automática de entradas do usuário (capitalização de nomes, IDs em maiúsculas, validação de formato de data).
* **Tratamento de Erros**: Uso de blocos `try-except` para lidar com entradas inválidas ou inconsistências de dados (ex: `ValueError` na validação de datas, `KeyError` ao buscar dados).
* **Programação Funcional (map e filter)**: Aplicação de `map` para transformar coleções de dados e `filter` para selecionar elementos com base em condições, utilizando funções `lambda`.
* **GUI com Tkinter**: Interface gráfica simples e intuitiva, com botões, menus e caixas de diálogo para interação com o usuário.


==============================
## 🛠️ Como Executar o Projeto
==============================

Para rodar o sistema em sua máquina, siga os passos abaixo:

1.  **Pré-requisitos**:
    * Python 3.x (recomenda-se Python 3.8 ou superior devido ao operador morsa `:=`)
    * Biblioteca Tkinter (geralmente já vem com a instalação padrão do Python)

2.  **Clone o Repositório (ou baixe os arquivos)**:
    Se você tiver o Git instalado:
    ```bash
    git clone <link_do_seu_repositorio>
    cd nome_da_pasta_do_projeto
    ```
    Ou baixe os arquivos zip e descompacte-os.

3.  **Estrutura de Arquivos**:
    Certifique-se de que os arquivos estejam organizados na seguinte estrutura:
    ```
    seu_projeto/
    ├── main.py
    ├── data_manager.py
    ├── event_functions.py
    ├── participant_functions.py
    ├── report_functions.py
    └── gui_elements.py
    ```

4.  **Executar o Sistema**:
    Abra o terminal (Prompt de Comando, PowerShell, Git Bash, etc.) na pasta raiz do projeto (`seu_projeto/`) e execute o arquivo principal:
    ```bash
    python main.py
    ```
    A janela do sistema de gerenciamento de eventos deverá ser exibida.

=====================
## 📝 Uso do Sistema
=====================

* Ao iniciar, o sistema estará vazio.
* Utilize a opção **`Arquivo -> Importar Dados (Exemplo)`** para carregar um conjunto de dados iniciais e começar a testar as funcionalidades.
* Explore os menus **`Eventos`**, **`Participantes`**, **`Relatórios e Estatísticas`** e **`Busca`** para acessar as diversas operações.
* Os botões na tela principal fornecem atalhos para as funcionalidades mais comuns.

---

**Autor**: Ana Clara Miguel dos Santos
**Data**: 04/07/2025
**Para**: Disciplina de Algoritmos e Lógica de Programação