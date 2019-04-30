from requests_html import HTMLSession

from src.classes.intrade_model import IntradeBarModel
from src.params.configure import Config
from utils.errors import OrderFailError


class IntradeBarWorker(IntradeBarModel):
    ses = HTMLSession()

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
        r = self.ses.post(self.url, data=self.form_data)

        if len(r.text) > 1:
            order_num = r.html.element('tr')

            print(f'Created order with № {order_num.attr.id}')
        else:
            raise ConnectionError(f'Failed to create an order: {r.text}')
