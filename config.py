import os

TASK_SERVICE_URL = os.getenv('TASK_SERVICE_URL',"http://localhost:5001")
BOOKMARK_SERVICE_URL = os.getenv("BOOKMARK_SERVICE_URL","http://localhost:5002")
EVENT_SERVICE_URL = os.getenv('EVENT_SERVICE_URL',"http://localhost:5003")

DEBUG = os.getenv('DEBUG','True') == 'True'
PORT = int(os.getenv('PORT', 5000))