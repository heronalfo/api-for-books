# Inicialização da Aplicação

Este guia fornece instruções sobre como inicializar a aplicação de gerenciamento de livros.

## Pré-requisitos

- Python 3.x instalado
- Pip (gerenciador de pacotes Python) instalado
- Ambiente virtual (opcional, mas recomendado)

## Passos

1. **Configurar Ambiente Virtual (Opcional):**
    - Recomenda-se configurar um ambiente virtual para isolar as dependências da aplicação. Execute os seguintes comandos:

    ```
    python -m venv venv
    source venv/bin/activate  # No Windows, use 'venv\Scripts\activate'
    ```

2. **Instalar Dependências:**
    - Com o ambiente virtual ativado, instale as dependências necessárias executando o seguinte comando:

    ```
    pip install -r requirements.txt
    ```

3. **Inicializar Banco de Dados:**
    - Certifique-se de que o banco de dados SQLite esteja configurado corretamente. Caso contrário, atualize a URL de conexão no arquivo `app.py`. Em seguida, inicialize o banco de dados executando o seguinte comando:

    ```
    python app.py
    ```

    Isso criará o arquivo do banco de dados SQLite especificado na URL de conexão.

4. **Executar Servidor Flask:**
    - Com todas as dependências instaladas e o banco de dados inicializado, execute o seguinte comando para iniciar o servidor Flask:

    ```
    python app.py
    ```

    O servidor Flask estará disponível em `http://localhost:5000/`.

5. **Acessar API:**
    - Uma vez que o servidor esteja em execução, você pode acessar a API utilizando as rotas definidas em `routes.py`. Por exemplo:
        - `GET http://localhost:5000/api/books/`: Retorna todos os livros.
        - `GET http://localhost:5000/api/books/<id>/`: Retorna um livro específico pelo ID.
        - `POST http://localhost:5000/api/books/insert_new_book/`: Insere um novo livro.
        - `DELETE http://localhost:5000/api/books/delete_book/<id>/`: Deleta um livro pelo ID.

6. **Desativar Ambiente Virtual (Opcional):**
    - Após finalizar o uso da aplicação, você pode desativar o ambiente virtual utilizando o seguinte comando:

    ```
    deactivate
    ```

Isso conclui os passos necessários para inicializar e utilizar a aplicação de gerenciamento de livros.