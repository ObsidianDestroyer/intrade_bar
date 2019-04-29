import requests

from src.classes.intrade_class import IntradeBarModel


class IntradeBarWorker(IntradeBarModel):
    def __init__(self, url):
        self.url = url
        self.form_data = {
            'user_id': self.user_id,
            'user_hash': self.user_hash,
            'option': self.option,
            'investment': self.investment,
            'time': self.time,
            'date': self.date,
            'trade_type': self.trade_type,
            'status': self.status
        }

    def make_call_order(self):
        r = requests.post(self.url, data=self.form_data)
        if len(r.text) > 1:
            pass
