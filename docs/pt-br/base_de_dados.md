---
## Documentação do Banco de Dados

### Estrutura da Tabela

A tabela `Books` possui os seguintes campos:

- **id (Integer, primary key)**: O identificador único do livro.
- **book (String, 100 caracteres, não nulo)**: O título do livro.
- **author (String, 200 caracteres, não nulo)**: O autor do livro.
- **synopsis (Text)**: A sinopse do livro.
- **created_at (Date, padrão: datetime.utcnow)**: A data de criação do registro.
- **content (Text, não nulo)**: O conteúdo do livro.

### Exemplo de Uso

1. **Inserir um novo livro**  
   ```python
   new_book = Books(
       book='Nome do Livro',
       author='Nome do Autor',
       synopsis='Sinopse do Livro',
       content='Conteúdo do Livro'
   )
   session.add(new_book)
   session.commit()
   ```

2. **Recuperar todos os livros**  
   ```python
   all_books = session.query(Books).all()
   for book in all_books:
       print(book.serialize())
   ```

3. **Recuperar um livro específico pelo ID**  
   ```python
   specific_book = session.query(Books).filter_by(id=1).first()
   print(specific_book.serialize())
   ```

4. **Atualizar um livro existente**  
   ```python
   book_to_update = session.query(Books).filter_by(id=1).first()
   book_to_update.book = 'Novo Título do Livro'
   session.commit()
   ```

5. **Excluir um livro pelo ID**  
   ```python
   book_to_delete = session.query(Books).filter_by(id=1).first()
   session.delete(book_to_delete)
   session.commit()
   ```

### Observações
- Certifique-se de configurar corretamente a conexão com o banco de dados no arquivo de configuração do SQLAlchemy.
- Use a função `serialize()` para converter objetos `Books` em dicionários serializados para facilitar a manipulação dos dados.

---