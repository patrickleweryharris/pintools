"""
TODO
"""

import os
import argparse
# import utils


def create_parser():
    """ Create argparse object for this CLI """
    parser = argparse.ArgumentParser(
        description=("TODO"))

    parser.add_argument("--pinboard_token", "-p", metavar="USER:KEY",
                        default=os.getenv("PINBOARD_API_TOKEN"),
                        help=("Pinboard API token. "
                              "Default: $PINBOARD_API_TOKEN"))

    subparser = parser.add_subparsers(dest="func")

    git_parser = subparser.add_parser("github", aliases=["g"],
                                      description="Copy Github Stars "
                                      "to Pinboard")

    git_parser.add_argument("--token", "-t", metavar="TOKEN",
                            default=os.getenv("PYGITHUB_ACCESS_TOKEN"),
                            help=("Github Access Token. "
                                  "Default: $PYGITHUB_ACCESS_TOKEN"))

    reddit_parser = subparser.add_parser("reddit", aliases=["r"],
                                         description="Copy saved Reddit "
                                         "items to Pinboard")

    reddit_parser.add_argument("username", metavar="USERNAME",
                               help="Reddit username")

    reddit_parser.add_argument("password", metavar="PASSWORD",
                               help="Reddit password")

    reddit_parser.add_argument("--secret", "-s", metavar="SECRET",
                               default=os.getenv('REDDIT_CLIENT_SECRET'),
                               help=("Reddit API secret. "
                                     "Default: $REDDIT_CLIENT_SECRET"))

    reddit_parser.add_argument("--client_id", "-c", metavar="CLIENT_ID",
                               default=os.getenv("REDDIT_CLIENT_ID"),
                               help=("Reddit API Client ID. "
                                     "Default: $REDDIT_CLIENT_ID"))

    tags_parser = subparser.add_parser("tags", aliases=["t"],
                                       description="Organize tags in Pinboard")

    tags_parser.add_argument('--config', "-c", metavar="CONFIG_FILE",
                             default=False,
                             help="Config file for tag organization")

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    print(args)
