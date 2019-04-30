from src.params.configure import Config

from oandapyV20 import API
from oandapyV20.endpoints.pricing import PricingStream


params = {
    "instruments": "EUR_USD"
}


class Streamer:
    api = API(
        access_token=Config.get_api_token(),
        environment='practice'
    )

    stream = PricingStream(
        accountID=Config.get_account_id(),
        params=params
    )

    def start_stream(self):
        rv = self.api.request(self.stream)
        return rv
