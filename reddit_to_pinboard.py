#!/usr/bin/env python
"""
Convert all saved Reddit links to Pinboard bookmarks
"""

import os
import argparse
import praw
import utils


def create_parser():
    """ Create argparse object for this CLI """
    parser = argparse.ArgumentParser(
        description=("Convert all saved Reddit links to Pinboard bookmarks"))

    parser.add_argument("username", metavar="USERNAME",
                        help="Reddit username")

    parser.add_argument("password", metavar="PASSWORD",
                        help="Reddit password")

    parser.add_argument("--secret", "-s", metavar="SECRET",
                        default=os.getenv('REDDIT_CLIENT_SECRET'),
                        help=("Reddit API secret. "
                              "Default: $REDDIT_CLIENT_SECRET"))

    parser.add_argument("--client_id", "-c", metavar="CLIENT_ID",
                        default=os.getenv("REDDIT_CLIENT_ID"),
                        help=("Reddit API Client ID. "
                              "Default: $REDDIT_CLIENT_ID"))

    parser.add_argument("--token", "-t", metavar="USER:KEY",
                        default=os.getenv("PINBOARD_API_TOKEN"),
                        help=("Pinboard API token. "
                              "Default: $PINBOARD_API_TOKEN"))
    return parser


def get_saved_links(username, password, secret, client_id):
    """
    Get all saved links from Reddit

    Parameters:
    username: str
        Reddit username
    password: str
        Reddit password
    secret: str
        Reddit API secret
    client_id: str
        Reddit API Client ID
    """
    user_agent = "/u/{} get all saved entries".format(username)
    print(user_agent)
    r = praw.Reddit(client_id=client_id, client_secret=secret,
                    password=password, username=username,
                    user_agent=user_agent)

    ret = []
    saved = r.user.me().saved(limit=10000)
    for item in saved:
        title = ""
        if hasattr(item, 'title'):
            title = item.title
        else:
            # Comments do not have titles
            title = "Comment on: {}".format(item.submission.title)

        it = {
            'title': title,
            'url': "https://reddit.com{}".format(item.permalink),
            'tags': ["reddit", item.subreddit.display_name],
            'extended': ""}
        ret.append(it)

    print("Found {} links to save to Pinboard".format(len(ret)))
    return ret


def main():
    parser = create_parser()
    args = parser.parse_args()
    links = get_saved_links(
        args.username,
        args.password,
        args.secret,
        args.client_id)
    utils.save_to_pinboard(args.token, links)


if __name__ == "__main__":
    main()
