import requests


def get_title(url):
    """ Gets the title of a URL """
    headers = {
        'headers': ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0)'
                    ' Gecko/20100101 Firefox/51.0')}
    dat = requests.get(url, headers=headers)
    dat = dat.text
    return dat[dat.find('<title>') + 7: dat.find('</title>')]


def fix_titles(pb, tag):
    """ Add correct title to all pinboard bookmarks with specified tag"""
    posts = pb.posts.all(tag=[tag])
    for post in posts:
        post.description = get_title(post.url)
        print("Correcting {} with new title {}".format(post.url,
                                                       post.description))
        post.save()
