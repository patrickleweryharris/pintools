#!/usr/bin/env python
"""
Convert all saved Reddit links to Pinboard bookmarks
"""

import praw
import pintools.utils as utils


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


def save_reddit_links(pinboard, username, pw, secret, client_id):
    """
    TODO
    """
    links = get_saved_links(
        username,
        pw,
        secret,
        client_id)
    utils.save_to_pinboard(pinboard, links)
