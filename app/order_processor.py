import requests

from datetime import datetime
from bs4 import BeautifulSoup as BS

from logger import log

vectors = {'call': 0, 'put': 1}


def perform_order(bid_cost, bid_vec, time_offset, settings):
    log.debug(f'Performing new order with BID COST: "{bid_cost}"')
    if bid_vec in vectors:
        bid_sets = {
            'user_id': settings['user_id'],
            'option': settings['option'],
            'time': time_offset,
            'date': datetime.now().strftime('%d-%m-%Y'),
            'trade_type': settings['trade_type'],
            'status': vectors[bid_vec],
            'user_hash': settings['user_hash'],
            'investment': bid_cost
        }
        process_order(bid_sets, settings['platform_url'])


def process_order(bid_set, platform_url):
    for k, v in vectors.items():
        if v == bid_set['status']:
            vector = k
    log.info(f'Processing new order with vector {vector}"')
    session = requests.Session()
    bid = session.post(platform_url, data=bid_set)
    bid_response = BS(bid.content.decode(), 'html.parser')
    if bid.status_code == '200':
        log.info(f'Bid id: {bid_response}')

    return

