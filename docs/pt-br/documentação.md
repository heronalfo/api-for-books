---
## Documentação da API

### Introdução
Esta documentação descreve a API para gerenciamento de livros. A API permite recuperar, inserir, editar e excluir informações sobre livros.

### Base URL
`/api/books/`

### Rotas
1. **GET /api/books/**  
   Recupera todos os livros.
   
2. **GET /api/books/<int:id>/**  
   Recupera um livro específico pelo seu ID.
   
3. **POST /api/books/insert_new_book/**  
   Insere um novo livro.
   
4. **DELETE /api/books/delete_book/<int:id>/**  
   Exclui um livro pelo seu ID.
   
5. **PATCH /api/books/edit_book/**  
   Edita um livro existente.

### Parâmetros de Requisição
- **id (int)**: O ID do livro.
- **book (str)**: O título do livro.
- **author (str)**: O autor do livro.
- **synopsis (str)**: A sinopse do livro.
- **content (str)**: O conteúdo do livro.

### Exemplos de Uso
1. **Recuperar todos os livros**  
   **Método**: GET  
   **URL**: `/api/books/`  
   **Resposta de Exemplo**:  
   ```
   [
       {
           "id": 1,
           "book": "Livro A",
           "author": "Autor A",
           "synopsis": "Sinopse do Livro A",
           "content": "Conteúdo do Livro A"
       },
       {
           "id": 2,
           "book": "Livro B",
           "author": "Autor B",
           "synopsis": "Sinopse do Livro B",
           "content": "Conteúdo do Livro B"
       }
   ]
   ```

2. **Recuperar um livro específico**  
   **Método**: GET  
   **URL**: `/api/books/1/`  
   **Resposta de Exemplo**:  
   ```
   {
       "id": 1,
       "book": "Livro A",
       "author": "Autor A",
       "synopsis": "Sinopse do Livro A",
       "content": "Conteúdo do Livro A"
   }
   ```

3. **Inserir um novo livro**  
   **Método**: POST  
   **URL**: `/api/books/insert_new_book/`  
   **Corpo da Requisição**:  
   ```
   {
       "book": "Novo Livro",
       "author": "Novo Autor",
       "synopsis": "Nova Sinopse",
       "content": "Novo Conteúdo"
   }
   ```  

4. **Excluir um livro**  
   **Método**: DELETE  
   **URL**: `/api/books/delete_book/1/`  
   **Resposta de Exemplo**:  
   ```
   {
       "message": "successfully deleted book",
       "status": 200
   }
   ```

5. **Editar um livro existente**  
   **Método**: PATCH  
   **URL**: `/api/books/edit_book/`  
   **Corpo da Requisição**:  
   ```
   {
       "id": 1,
       "book": "Livro Editado",
       "author": "Autor Editado",
       "synopsis": "Sinopse Editada",
       "content": "Conteúdo Editado"
   }
   ```

### Respostas de Exemplo
- **200 OK**: A requisição foi bem-sucedida.
- **400 Bad Request**: A requisição é inválida ou está faltando parâmetros.
- **404 Not Found**: O recurso solicitado não foi encontrado.
- **405 Method Not Allowed**: O método de requisição não é permitido para o recurso solicitado.

---