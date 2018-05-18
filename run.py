from flask import Flask, request, abort
from gevent.wsgi import WSGIServer
import config
import json

from dispatcher import Dispatcher

'''
App. Starting server and handling http requests.
'''

app = Flask(__name__)
dispatcher = Dispatcher(
    api_url = config.METEO_API,
    token = config.METEO_TOKEN
)

# handling message on GET: /forecast
@app.route('/forecast', methods = ['GET'])
def handle_forecast():
  if request.method == 'GET':
    query = request.get_json()
    return dispatcher.forecast(query)

@app.route('/current', methods = ['GET'])
def handle_current():
    if request.method == 'GET':
        query = request.get_json()
        return dispatcher.current(query)

if __name__ == '__main__':
  server = WSGIServer((config.HOST, config.PORT), app)
  print('Python starting at {0}:{1}'.format(config.HOST, config.PORT))
  server.serve_forever()