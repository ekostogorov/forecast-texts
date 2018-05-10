import requests

API_REQ_ERR = 'Request to API failed'

class DataModuleMapper(object):
    _url = None
    _token = None
    def __init__(self, api_url, token):
        self._url = api_url
        self._token = token

    def get_forecast(self, params):
        city = params['city']
        url = self._url + '/' + self._token + '/forecast/q/CA/' + city + '.json'
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            raise Exception(API_REQ_ERR)