import logging

from os import environ
from colorlog import ColoredFormatter

__all__ = ['log']
_LOG_LEVEL = (
    logging.NOTSET
    if not environ.get('LOG_LEVEL')
    and bool(environ.get('LOGGING')) is not True
    else environ.get('LOG_LEVEL')
)

_LOG_FORMAT = '  %(log_color)s%(levelname)-8s%(reset)s[%(name)s-> %(funcName)s:%(lineno)d ]%(log_color)s %(message)s%(reset)s'  # noqa: E501


def _logger_init():
    logging.root.setLevel(_LOG_LEVEL)
    formatter = ColoredFormatter(_LOG_FORMAT)
    stream = logging.StreamHandler()
    stream.setLevel(_LOG_LEVEL)
    stream.setFormatter(formatter)
    log_ = logging.getLogger(__name__)
    log_.setLevel(_LOG_LEVEL)
    log_.addHandler(stream)

    return log_


log = _logger_init()
