import os
import sys
import yaml
import json
import asyncio
import requests

from datetime import datetime, timedelta

from logger import log
from order_processor import perform_order

# Logger name
log.name = __name__


CONFIG_PATH = os.getenv('CONFIG_PATH', './app/params/params.yml')

# Bot settings
settings = {}


def read_config() -> None:
    try:
        log.info(f'Starting read config file: {CONFIG_PATH}')

        with open(CONFIG_PATH, 'r') as config:
            config_data = yaml.load(config, Loader=yaml.Loader)

            log.info(f'Loaded settings from: {CONFIG_PATH}')
            settings.update(config_data)

    except FileNotFoundError as f_err:
        if 'CONFIG_PATH' not in os.environ:
            log.critical(f'While locating config '
                         f'file occurred error: {f_err.__context__ or f_err}')
        else:
            log.critical(f'Failed to locate config file in path: {CONFIG_PATH}')
        return sys.exit(1)


def set_time_offset(offset=5) -> str:
    return datetime.strftime(datetime.now() + timedelta(
        minutes=offset if offset != 5 else offset), '%H:%M')


def get_tickers() -> dict:
    session = requests.Session()
    try:
        rates = json.loads(session.get(settings['platform_rates']).content)
        yield rates

    except json.JSONDecodeError as j_err:
        log.error(f'Failed to read json stream with error: {j_err.__context__ or j_err}')


async def main():
    read_config()
    perform_order(10, settings)
    log.warning(settings['token'])

if __name__ == '__main__':
    try:
        log.debug('Getting main event loop . . .')
        loop = asyncio.get_event_loop()

        log.info('Starting application . . .')
        loop.run_until_complete(main())

    except KeyboardInterrupt:
        log.warning('Application stopped by user!')

