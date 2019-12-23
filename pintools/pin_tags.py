"""
Adds the domain name as a tag for all pinboard bookmarks,
so I can organise by site
"""

import os
import yaml
from urllib.parse import urlparse


def replace_stuff(url):
    """ Remove common domain suffixes and prefixes """
    stuff = ['www.', 'm.', 'blog.', 'help.', 'blogs.',
             'gist.', 'en.', '.co', 'www2.', '.wordpress']
    for item in stuff:
        url = url.replace(item, '')

    return url


def process_domain_assoc(url, domain_map):
    """
    Replace domain name with a more fitting tag for that domain.
    User defined. Mapping comes from provided config file

    Mapping in yml file is as follows:
    tag:
        - url to map to tag
        - ...

    A small example domain_assoc.yml is included
    """
    if not domain_map:
        return url

    for key in domain_map:
        if url in domain_map[key]:
            return key

    return url


def pin_tags(pb, config_file):
    """
    Tag every item in pinboard with the name of it's
    originating website
    """
    all_bookmarks = pb.posts.all()

    # Boolean to determine wheter to do additional filtering
    # Only run if filter config file exists
    domain_map = None
    if config_file and os.path.isfile(config_file):
        f = open(config_file, "r")
        domain_map = yaml.safe_load(f)['domains']

    for bookmark in all_bookmarks:
        url = bookmark.url
        tags = bookmark.tags
        parsed = urlparse(url).netloc
        parsed = parsed[:parsed.rfind('.')]

        parsed = replace_stuff(parsed)
        parsed = process_domain_assoc(parsed, domain_map)

        if parsed not in tags:
            print("=============================================")
            print("Bookmark: {}".format(bookmark.description))
            print("Tags to add: {}".format(parsed))
            print("Current tags: {}".format(tags))
            tags = [parsed] + tags
            bookmark.tags = tags
            print("New tags: {}".format(bookmark.tags))
            bookmark.save()
            print("=============================================")
