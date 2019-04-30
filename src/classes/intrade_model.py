from src.params.configure import Config

from datetime import datetime, timedelta


class IntradeBarModel:
    @property
    def user_id(self) -> int:
        return 55603

    @property
    def user_hash(self) -> str:
        return Config.get_api_token()

    @property
    def option(self) -> str:
        return 'EURCAD'

    @property
    def investment(self) -> str:
        return 95

    @property
    def time(self):
        return Config.get_current_time()

    @property
    def date(self) -> str:
        return datetime.strftime(datetime.today(), '%d-%m-%Y')

    @property
    def trade_type(self) -> str:
        return 'classic'

    @property
    def status(self) -> int:
        return 2
