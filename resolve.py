#!/usr/bin/env python

import sys
import argparse
import configparser

import twitter

def run():
    parser = argparse.ArgumentParser(description='Converts Twitter Usernames to UIDs.')
    parser.add_argument('-c', dest='configfile', type=str, help='Config file path',
                        default='config.ini')
    parser.add_argument('inputfile', type=str, nargs='?', help='Username input file')
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.configfile)

    oauth = {
        'ACCESS_TOKEN_KEY': config['twitter.com']['ACCESS_TOKEN_KEY'],
        'ACCESS_TOKEN_SECRET': config['twitter.com']['ACCESS_TOKEN_SECRET'],
        'CONSUMER_KEY': config['twitter.com']['CONSUMER_KEY'],
        'CONSUMER_SECRET': config['twitter.com']['CONSUMER_SECRET']
    }

    api = twitter.Api(consumer_key=oauth['CONSUMER_KEY'],
                      consumer_secret=oauth['CONSUMER_SECRET'],
                      access_token_key=oauth['ACCESS_TOKEN_KEY'],
                      access_token_secret=oauth['ACCESS_TOKEN_SECRET'],
                      sleep_on_rate_limit=True)

    if args.inputfile:
        users = open(args.inputfile)
    else:
        users = sys.stdin

    for user in users:
        while True:
            user = user.strip()
            try:
                blocked = api.CreateBlock(screen_name=user, include_entities=False,
                                          skip_status=True)
                print('%s->%s BLOCKED' % (user, blocked.id))
                break
            except twitter.error.TwitterError as err:
                print("error: twitter: %s" % (err), file=sys.stderr)
                break
            except OSError as err:
                # probably network down
                print("error: general: %s" % (err), file=sys.stderr)

    users.close()

if __name__ == '__main__':
    run()
