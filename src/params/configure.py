from yaml import Loader, load
from os import listdir
from glob import glob

from datetime import datetime, timedelta

config_path = glob('configuration.yml').pop(0)


def get_config():
    if config_path in listdir():
        data_loaded = load(open(config_path))
        return data_loaded


class Config:
    def __init__(self, *file):
        self.file = file

    @staticmethod
    def get_current_time(**offset: str) -> str:
        """
        Standard offset is 10 minutes from now
        """
        if offset:
            return datetime.strftime((datetime.now() + timedelta(minutes=offset)), '%H:%M')

        # default offset
        return datetime.strftime((datetime.now() + timedelta(minutes=10)), '%H:%M')

    @staticmethod
    def get_api_token():
        f = get_config()
        return f['token']

    @staticmethod
    def get_account_id():
        f = get_config()
        return f['active_account']

