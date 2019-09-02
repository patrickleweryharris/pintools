import pinboard


def save_to_pinboard(api_token, links):
    """
    Save new links to pinboard

    Parameters:
    api_token: str
        Pinboard API token
    links: [{title, url, tags, extended}]
        Information about link
    """
    pb = pinboard.Pinboard(api_token)

    for link in links:
        print("Saving: {}".format(link.get('title')))

        pb.posts.add(url=link.get('url'),
                     description=link.get('title'),
                     tags=link.get('tags'),
                     extended="{} via https://plh.io/pinboard".format(
                         link.get('extended')),
                     shared=False,
                     toread=False)
