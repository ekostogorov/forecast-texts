class Dispatcher(object):
    api_url = None
    def __init__(self, api_url):
        self.api_url = api_url
    
    def forecast(self, query):
        print("Query is", query)
        return True