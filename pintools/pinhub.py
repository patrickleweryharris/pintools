#!/usr/bin/env python
"""
Export Github stars to Pinboard bookmarks
"""

import github
import pintools.utils as utils

GITHUB = "https://github.com"


def get_github_stars(token):
    """
    Return Github stars for a user

    Parameters
    ==========
    token: str
        Github Access Token
    return: str
    """
    g = github.Github(token)

    g = g.get_user()
    names = [(item.full_name, item.description) for item in g.get_starred()]
    return names


def save_git_stars(pinboard, github_token):
    """
    TODO
    """
    stars = get_github_stars(github_token)
    stars = [{'title': star[0],
              'url': "{}/{}".format(GITHUB,
                                    star[0]),
              'extended': star[1],
              'tags': ["github", "git_stars"]} for star in stars]
    utils.save_to_pinboard(pinboard, stars)
