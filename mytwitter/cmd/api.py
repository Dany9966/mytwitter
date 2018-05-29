import argparse

import mytwitter.config

from mytwitter import api
from mytwitter.client import rpc
from mytwitter import log

CONF = mytwitter.config.CONF

parser = argparse.ArgumentParser(description='mytwitter RPC client.')
parser.add_argument('--config-path', required=True,
                    help='The config file path.')


def main():
    args = parser.parse_args()

    CONF.load_config(args.config_path)
    log.configure_logging()

    api.app.run(host='0.0.0.0', port=CONF.api.port)
