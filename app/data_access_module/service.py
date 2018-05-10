from mapper import DataModuleMapper

class DataModuleService(object):
    mapper = None
    def __init__(self, api_url):
        self.mapper = DataModuleMapper(api_url)

    def get_forecast(self, params):
        return self.mapper.get_forecast(params)