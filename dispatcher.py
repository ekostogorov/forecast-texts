from app.data_access_module import DataModuleFacade

class Dispatcher(object):
    api_url = None
    data_access_module = None
    def __init__(self, api_url, token):
        self.data_access_module = DataModuleFacade(
            api_url = api_url,
            token = token
        )
    
    def forecast(self, query):
        print("Query is", query)
        return True