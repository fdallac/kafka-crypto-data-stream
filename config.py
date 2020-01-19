# config

params = {
        # crypto setup
        'currency_1': 'BTC', # bitcoin
        'currency_2': 'ETH', # ethereum
        'currency_3': 'LINK', # chainlink
        'ref_currency': 'USD',
        'ma': 25,
        # api setup
        'api_call_period': 5,
}

config = {
        # api auth
        'api_key': ':)',
        'api_secret': ':)',
        'api_pass': ':)',
        # kafka
        'kafka_broker': 'localhost:9092',
        # topics
        'topic_1': 'topic_{0}'.format(params['currency_1']),
        'topic_2': 'topic_{0}'.format(params['currency_2']),
        'topic_3': 'topic_{0}'.format(params['currency_3']),
        'topic_4': 'topic_{0}_ma_{1}'.format(params['currency_1'], params['ma']),
        'topic_5': 'topic_{0}_ma_{1}'.format(params['currency_2'], params['ma']),
        'topic_6': 'topic_{0}_ma_{1}'.format(params['currency_3'], params['ma']),
}

