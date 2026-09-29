# API de Relatórios Financeiros

Projeto desenvolvido em Python e FastAPI com o objetivo de praticar uma estrutura de backend mais organizada, saindo de scripts lineares e separando melhor as responsabilidades da aplicação.
A API utiliza Redis e RQ para colocar tarefas mais pesadas em uma fila e processá-las em segundo plano através de um worker.

- Arquitetura
O projeto foi dividido em algumas camadas para evitar que toda a lógica fique concentrada nas rotas:
- Routes: recebem as requisições HTTP e retornam as respostas.
- Services: concentram as regras de negócio e as validações.
- Repositories: responsáveis pelo acesso e persistência dos dados.
- Database: gerenciamento das conexões com o banco de dados.
- Utils: funções auxiliares, incluindo logs e auditoria.
- Worker: responsável por executar as tarefas que foram colocadas na fila.

A ideia principal é manter cada parte da aplicação com uma responsabilidade específica, facilitando a manutenção e futuras alterações.

Tecnologias
- Python
- FastAPI
- Redis
- RQ (Redis Queue)
- Docker
- Docker Compose

## Como funciona:
O fluxo básico da geração de um relatório é:
O cliente faz uma requisição para a API.
A rota encaminha a operação para o service.
O service realiza as validações necessárias e consulta os dados através do repository.
A tarefa de geração do relatório é enviada para uma fila no Redis.
A API retorna a resposta sem precisar esperar todo o processamento.
O worker pega a tarefa da fila e executa o processamento em segundo plano.

## Como executar:
Pré-requisitos
Python instalado
Docker
Docker Compose

1. Iniciar o Redis
Na raiz do projeto:
docker-compose up -d
2. Criar o ambiente virtual
python3 -m venv venv
No macOS/Linux:
source venv/bin/activate
No Windows:
venv\Scripts\activate
3. Instalar as dependências
pip install -r requirements.txt
4. Iniciar a API
python -m app.main
A API ficará disponível em:
http://localhost:8000
A documentação do FastAPI pode ser acessada em:
http://localhost:8000/docs
5. Iniciar o worker
Em outro terminal, com o ambiente virtual ativado:
rq worker fila_relatorios
O worker ficará responsável por consumir as tarefas da fila e executar o processamento dos relatórios.


## O que pratiquei neste projeto:

Organização de projetos Python<br>
Arquitetura em camadas<br>
Separação de responsabilidades<br>
Desenvolvimento de APIs com FastAPI<br>
Redis<br>
Filas com RQ<br>
Processamento em background<br>
Gerenciamento de conexões com banco de dados<br>
Logs e auditoria<br>
Docker e Docker Compose

```markdown
## Estrutura do projeto
app/
├── routes/
├── services/
├── repositories/
├── database/
├── utils/
├── worker/
└── main.py

requirements.txt
docker-compose.yml
README.md
