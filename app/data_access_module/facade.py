from service import DataModuleService

class DataModuleFacade(object):
    service = None
    def __init__(self, api_url, token):
        self.service = DataModuleService(
            api_url = api_url,
            token = token
        )

    def get_forecast(self, params):
        return self.service.get_forecast(params)