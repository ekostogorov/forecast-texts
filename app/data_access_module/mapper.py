class DataModuleMapper(object):
    url = None
    def __init__(self, api_url):
        self.url = api_url

    def get_forecast(self, params):
        return True