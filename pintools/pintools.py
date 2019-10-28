"""
TODO
"""

import os
import argparse

import pinboard

from pintools.pinhub import save_git_stars
from pintools.reddit_to_pinboard import save_reddit_links
from pintools.title_fix import fix_titles

__version__ = "0.0.3"

desc = """ Command line tools for working with Pinboard.
           Allows copying of Github Stars and Reddit Saved posts
           to Pinboard, as well as organizing tags based on originating
           site """


def create_parser():
    """ Create argparse object for this CLI """
    parser = argparse.ArgumentParser(
        description=desc)

    parser.add_argument("--pinboard_token", "-p", metavar="USER:KEY",
                        default=os.getenv("PINBOARD_API_TOKEN"),
                        help=("Pinboard API token. "
                              "Default: $PINBOARD_API_TOKEN"))

    parser.add_argument("--version", "-v", action="store_true",
                        default=False,
                        help="Return version information")

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

    titles_parser = subparser.add_parser("titles",
                                         description=("Correct bookmark titles"
                                                      "for a specific tag. The"
                                                      "title of the URL is"
                                                      "assumed to be the"
                                                      "correct"
                                                      "title"))

    titles_parser.add_argument("--tag", "-t", metavar="TAG",
                               default=False,
                               help="Tag to fix all titles for")

    return parser


def run_options(args):
    """
    Run functions that the user has specified
    """
    pb = pinboard.Pinboard(args.pinboard_token)

    if args.version:
        print(__version__)
        return
    if args.func in ["github", "g"]:
        print("Saving Github stars to Pinboard...")
        save_git_stars(pb, args.token)
    elif args.func in ["reddit", "r"]:
        print("Saving Reddit saved links to Pinboard...")
        save_reddit_links(pinboard, args.username, args.password, args.secret,
                          args.client_id)
    elif args.func in ["tags", "t"]:
        print("Not yet implemented")
    elif args.func in ["titles"]:
        if not args.tag:
            print("Please specify a tag to fix titles for")
            return
        fix_titles(pb, args.tag)
    else:
        print("No argument specified, use -h for help")


def main():
    parser = create_parser()
    args = parser.parse_args()
    run_options(args)


if __name__ == "__main__":
    main()
