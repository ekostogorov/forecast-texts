from forecast_service import ForecastService

class DataModuleFacade(object):
    forecast_service = None
    current_service = None
    def __init__(self, api_url, token):
        self.forecast_service = DataModuleService(
            api_url = api_url,
            token = token
        )

    def get_forecast(self, params):
        return self.forecast_service.get(params)