from forecast_mapper import ForecastMapper

class ForecastService(object):
    forecast_mapper = None
    def __init__(self, api_url, token):
        self.forecast_mapper = ForecastMapper(
            api_url = api_url,
            token = token
            )

    def get(self, params):
        return self.forecast_mapper.get_forecast(params)