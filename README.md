# API Gateway - App de Produtividade

## Descrição
Este é o serviço de API Gateway para o App de Produtividade. Ele atua como ponto de entrada centralizado para todos os microsserviços da aplicação, gerenciando o roteamento de requisições e a comunicação entre os serviços.

## Arquitetura do Projeto
O App de Produtividade é composto pelos seguintes microsserviços:
1. **API Gateway** - Ponto de entrada centralizado para a aplicação
2. **Task Service** - Gerenciamento de tarefas e prioridades
3. **Event Service** - Gerenciamento de eventos e calendário
4. **Bookmark Service** - Gerenciamento de favoritos/bookmarks
5. **Frontend** - Interface de usuário da aplicação

## Requisitos
- Python 3.8+
- Flask
- Outras dependências listadas em `requirements.txt`

## Instalação

### Configuração do ambiente virtual

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (Windows)
venv\Scripts\activate

# Ativar ambiente virtual (Linux/Mac)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt


## Execução
```bash
# Ativar ambiente virtual (se ainda não estiver ativado)
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Executar o serviço
python app.py
```

Por padrão, o serviço estará disponível em `http://localhost:5000`.

## Endpoints
- `/api/task` - Roteamento para o serviço de tarefas
- `/api/event` - Roteamento para o serviço de eventos
- `/api/bookmark` - Roteamento para o serviço de bookmarks

## Configuração
As configurações do serviço estão no arquivo `config.py`. Você pode ajustar as seguintes variáveis:
- Portas dos serviços
- URLs dos serviços
- Outras configurações específicas

## Docker
Para executar este serviço usando Docker:

```bash
# Construir a imagem
docker build -t productivity-api-gateway .

# Executar o container
docker run -p 5000:5000 productivity-api-gateway
```

## Comunicação com outros serviços
Este gateway se comunica com os seguintes serviços:
- Task Service (porta 5001)
- Event Service (porta 5002)
- Bookmark Service (porta 5003)

Certifique-se de que esses serviços estejam em execução para o funcionamento completo da aplicação.
