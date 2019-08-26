#!/usr/bin/env python
"""
Export Github stars to Pinboard bookmarks
"""

import os
import argparse
import github
import utils

GITHUB = "https://github.com"


def create_parser():
    """ Create argparse object for this CLI """
    parser = argparse.ArgumentParser(
        description=("Copy Github Stars to Pinboard"))

    parser.add_argument("--pinboard_token", "-p", metavar="USER:KEY",
                        default=os.getenv("PINBOARD_API_TOKEN"),
                        help=("Pinboard API token. "
                              "Default: $PINBOARD_API_TOKEN"))

    parser.add_argument("--github_token", "-g", metavar="TOKEN",
                        default=os.getenv("PYGITHUB_ACCESS_TOKEN"),
                        help=("Github Access Token. "
                              "Default: $PYGITHUB_ACCESS_TOKEN"))
    return parser


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
    names = [item.full_name for item in g.get_starred()]
    return names


def main():
    parser = create_parser()
    args = parser.parse_args()
    stars = get_github_stars(args.github_token)
    stars = [{'title': star,
              'url': "{}/{}".format(GITHUB,
                                    star),
              'tags': ["github", "git_stars"]} for star in stars]
    utils.save_to_pinboard(args.pinboard_token, stars)


if __name__ == "__main__":
    main()
