# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST com FastAPI para gerenciar tarefas e pratique como definir rotas, validar dados e responder com os códigos HTTP apropriados.

## 📝 Tarefas

### 🛠️ Criar a primeira rota da API

#### Descrição

Crie uma aplicação FastAPI e implemente uma rota `GET /health` que indique que a API está funcionando. Execute a aplicação localmente com Uvicorn e consulte a rota pelo navegador ou por uma ferramenta HTTP.

#### Requisitos

A aplicação concluída deve:

- Criar uma instância de `FastAPI`
- Retornar `{"status": "ok"}` ao receber uma requisição `GET /health`
- Iniciar localmente com Uvicorn e permitir que a rota seja consultada

### 🛠️ Implementar operações CRUD para tarefas

#### Descrição

Expanda a API para gerenciar tarefas em memória. Cada tarefa deve ter um identificador, um título e um indicador de conclusão. Use modelos do Pydantic para definir os dados aceitos e retornados.

#### Requisitos

A aplicação concluída deve:

- Definir um modelo de tarefa com `id`, `title` e `completed`
- Implementar `GET /tasks` para listar tarefas e `GET /tasks/{task_id}` para buscar uma tarefa pelo identificador
- Implementar `POST /tasks` para criar uma tarefa, `PUT /tasks/{task_id}` para atualizar uma tarefa e `DELETE /tasks/{task_id}` para removê-la
- Manter as tarefas em memória durante a execução da aplicação

### 🛠️ Validar entradas e tratar respostas HTTP

#### Descrição

Aprimore os endpoints para que clientes da API recebam respostas previsíveis quando enviam dados inválidos ou solicitam tarefas inexistentes. Verifique os resultados pela documentação interativa do FastAPI ou por testes HTTP.

#### Requisitos

A aplicação concluída deve:

- Recusar títulos vazios ou compostos apenas por espaços
- Retornar `201 Created` ao criar uma tarefa e `204 No Content` ao removê-la com sucesso
- Retornar `404 Not Found` quando o identificador solicitado não existir
- Retornar `422 Unprocessable Entity` para dados que não atendam à validação do modelo
