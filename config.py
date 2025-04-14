import os

# Endereços dos microserviços dentro da mesma rede Docker
TASK_SERVICE_URL = os.getenv('TASK_SERVICE_URL', 'http://tasks:5001')
BOOKMARK_SERVICE_URL = os.getenv('BOOKMARK_SERVICE_URL', 'http://bookmarks:5002')
EVENT_SERVICE_URL = os.getenv('EVENT_SERVICE_URL', 'http://event:5003')

DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
PORT = int(os.getenv('PORT', 5000))
