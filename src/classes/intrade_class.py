from datetime import datetime, timedelta


class IntradeBarModel:
    @property
    def user_id(self) -> int:
        return 55603

    @property
    def user_hash(self) -> str:
        return '14a6ab43cca40185cf41cc3b2a94937f'

    @property
    def option(self) -> str:
        return 'EURCAD'

    @property
    def investment(self) -> str:
        return 95

    @property
    def time(self) -> str:
        return datetime.strftime((datetime.now() + timedelta(minutes=10)), '%H:%M')

    @property
    def date(self) -> str:
        return datetime.strftime(datetime.today(), '%d-%m-%Y')

    @property
    def trade_type(self) -> str:
        return 'classic'

    @property
    def status(self) -> int:
        return 2
