# AnimalFinder

**Site**:
https://animalfinderproject.herokuapp.com/


**Ferramentas utilizadas**:
- Linguagem: python3
- Framework: django3
- Serviço cloud: Heroku
- Api rest: djangorestframework


**Banco de dados**:

O site vem com alguns animais e donos pré-cadastrados com o objetivo de verificar os critérios como paginação funcionalidade do "Encontrei".

Usuários cadastrados:
- Email= a@gmail.com   senha: a
- Email= b@gmail.com   senha: b
- Email= c@gmail.com   senha: c

Usuário administrador: para acessar o banco de dados como administrador (apenas para critérios de análise): vá em
127.0.0.1:8000/admin e faça login com os seguintes dados:

email: a@gmail.com
senha: a

**API REST**:

para visualizar o formato json de todos os animais perdidos, basta enviar um request do tipo GET para **127.0.0.1:8000/api/usuario**. A api foi configurada para que seja enviado apenas os animais perdidos, mas pode ser alterado para mostrar todos os animais com uma pequena alteração.
