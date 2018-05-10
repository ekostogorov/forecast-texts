from service import DataModuleService

class DataModuleFacade(object):
    service = None
    def __init__(self, api_url):
        self.service = DataModuleService(
            api_url
        )

    def get_forecast(self, params):
        return self.service.get_forecast(params)