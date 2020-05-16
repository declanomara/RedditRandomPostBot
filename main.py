import configparser
import argparse
import praw
import random
import os

from praw.exceptions import WebSocketException


if __name__ == '__main__':
    cfg = configparser.ConfigParser()
    cfg.read('config.ini')

    client_id = cfg['DEFAULT']['client_id']
    client_secret = cfg['DEFAULT']['client_secret']
    username = cfg['DEFAULT']['username']
    password = cfg['DEFAULT']['password']
    user_agent = cfg['DEFAULT']['user_agent']

    r = praw.Reddit(client_id=client_id,
                    client_secret=client_secret,
                    user_agent=user_agent,
                    username=username,
                    password=password)
    r.validate_on_submit = True

    parser = argparse.ArgumentParser()
    parser.add_argument('--subreddit', default='mxethaephfouer', dest='subreddit')
    parser.add_argument('--words', default='words.txt', dest='words')
    parser.add_argument('--images', default='images', dest='images')
    parser.add_argument('--count', type=int, default=10, dest='count')

    args = parser.parse_args()

    f = []
    for (dirpath, dirnames, filenames) in os.walk(args.images):
        f.extend(filenames)
        break

    images = [f'{args.images}/{file}' for file in f]
    words = []
    with open(args.words, 'r') as f:
        words.extend([w.strip('\n') for w in f.readlines()])

    if r.read_only:
        print('Failed to authenticate with Reddit')
        quit(1)

    sub = r.subreddit(args.subreddit)

    for i in range(args.count):
        title = f'{random.choice(words)} {random.choice(words)}'
        file = random.choice(images)
        print(f'Submitting post with title "{title}" and image "{file}"')
        try:
            sub.submit_image(title, file)

        except WebSocketException:
            print('An error occurred, but the post was most likely still submitted')

