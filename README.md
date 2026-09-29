# API de Relatórios Financeiros

Projeto desenvolvido para consolidar a transição de scripts lineares para uma arquitetura de backend profissional em Python e FastAPI. O objetivo principal foi estruturar um sistema desacoplado, modular e preparado para lidar com processamento assíncrono de tarefas pesadas.

## Decisões Arquiteturais

O projeto foi construído seguindo uma separação estrita de responsabilidades entre as camadas:

- **Rotas (Routes):** Camada de entrada responsável exclusivamente por receber as requisições HTTP do cliente e retornar respostas rápidas.
- **Serviços (Services):** Camada onde residem as regras de negócio e validações, delegando o processamento pesado para o sistema de filas.
- **Repositórios (Repositories):** Camada responsável pela persistência e comunicação com a base de dados.
- **Banco de Dados (Database):** Gestão centralizada de conexões utilizando gerenciadores de contexto (`contextlib`) para garantir o fechamento seguro de recursos e evitar vazamentos.
- **Utuilitários (Utils):** Módulo centralizado de auditoria e logs estruturados para monitoramento das operações.

## Tecnologias Utilizadas

- **Python**
- **FastAPI** (Construção da API e documentação automática via Swagger)
- **Redis** (Message broker para gerenciamento de filas)
- **RQ (Redis Queue)** (Background workers para processamento assíncrono)
- **Docker e Docker Compose** (Isolamento e subida da infraestrutura)

## Fluxo de Funcionamento

1. O cliente faz uma requisição POST na rota de relatórios através da API.
2. A camada de rotas aciona o serviço, que valida as regras de negócio consultando o repositório e o banco de dados de forma segura.
3. O serviço despacha a tarefa de geração do relatório para a fila do Redis e retorna uma resposta de sucesso imediata para o cliente.
4. Um worker em segundo plano consome a tarefa da fila, executando o processamento pesado de forma assíncrona sem impactar a performance da API.

## Como Executar o Projeto

### Pré-requisitos
- Python instalado na máquina
- Docker e Docker Compose configurados

### 1. Subir a infraestrutura (Redis)
Na raiz do projeto, inicie o container do Redis:
docker-compose up -d
2. Configurar o ambiente virtual e dependências
Crie e ative o ambiente virtual:
Bash
python3 -m venv venv
source venv/bin/activate
Instale as dependências do projeto:
Bash
pip install -r requirements.txt
3. Iniciar a API
Execute o servidor da aplicação a partir da raiz:
Bash
python -m app.main
Acesse a documentação interativa em: http://localhost:8000/docs
4. Iniciar o Background Worker
Em um segundo terminal (com o ambiente virtual ativo), execute o worker para processar as filas:
Bash
rq worker fila_relatorios
