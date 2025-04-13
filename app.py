from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
from config import TASK_SERVICE_URL, BOOKMARK_SERVICE_URL, EVENT_SERVICE_URL, DEBUG, PORT

app = Flask(__name__)
CORS(app)

# Função modificada para encaminhar requisições
def forward_request(service_url, endpoint, method):
    """
    Encaminha uma requisição para o serviço especificado.

    Args:
        service_url: URL base do serviço de destino
        endpoint: Endpoint completo (ex: /api/tasks)
        method: Método HTTP (GET, POST, etc.)
    """
    # Constrói a URL completa para o serviço
    url = f"{service_url}{endpoint}"

    print(f"Encaminhando para: {url}, método: {method}")

    # Encaminha a requisição mantendo o método, headers e dados
    response = requests.request(
        method=method,
        url=url,
        headers={key: value for key, value in request.headers if key != 'Host'},
        data=request.get_data(),
        params=request.args
    )

    # Retorna a resposta do serviço
    return (
        response.content,
        response.status_code,
        response.headers.items()
    )

# Rotas específicas para o serviço de tarefas
@app.route('/api/task', methods=['GET', 'POST', 'PUT', 'DELETE'])
def task_single():
    return forward_request(TASK_SERVICE_URL, '/api/task', request.method)

@app.route('/api/tasks', methods=['GET'])
def tasks_list():
    return forward_request(TASK_SERVICE_URL, '/api/tasks', request.method)

# Rotas específicas para o serviço de bookmarks
@app.route('/api/bookmark', methods=['GET', 'PUT', 'DELETE'])
def bookmark_single():
    return forward_request(BOOKMARK_SERVICE_URL, '/api/bookmark', request.method)

@app.route('/api/bookmarks', methods=['GET', 'POST'])
def bookmarks_list():
    return forward_request(BOOKMARK_SERVICE_URL, '/api/bookmarks', request.method)

# Rotas específicas para o serviço de eventos
@app.route('/api/event', methods=['GET', 'POST', 'PUT', 'DELETE'])
def event_single():
    return forward_request(EVENT_SERVICE_URL, '/api/event', request.method)

@app.route('/api/events', methods=['GET'])
def events_list():
    return forward_request(EVENT_SERVICE_URL, '/api/events', request.method)

# Rota de status do gateway
@app.route('/api/status', methods=['GET'])
def status():
    """
    Rota que verifica o status de todos os serviços.
    """
    services = {
        'task_service': {'url': TASK_SERVICE_URL},
        'bookmark_service': {'url': BOOKMARK_SERVICE_URL},
        'calendar_service': {'url': EVENT_SERVICE_URL}
    }

    for name, service in services.items():
        try:
            response = requests.get(f"{service['url']}/health", timeout=2)
            service['status'] = 'online' if response.status_code == 200 else 'error'
        except requests.RequestException:
            service['status'] = 'offline'

    return jsonify({
        'gateway': 'online',
        'services': services
    })

# Rota raiz para verificação
@app.route('/', methods=['GET'])
def root():
    return jsonify({
        "message": "API Gateway está funcionando",
        "status": "online",
        "endpoints": [
            "/api/status",
            "/api/task", "/api/tasks",
            "/api/bookmark", "/api/bookmarks",
            "/api/event", "/api/events"
        ]
    })

if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)