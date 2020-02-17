![](https://github.com/patrickleweryharris/pintools/workflows/Python%20package/badge.svg)
![](https://img.shields.io/pypi/v/pintools)

# Pintools
Command line tools for working with [Pinboard](https://pinboard.in).

Features:
- Import starred repositories from Github
- Copy saved reddit links
- Organize tags based on originating site
- Title fixer

## Install

```
pip install pintools
```

### Dev install

Requires [pre-commit](https://pre-commit.com/)

```
$ git clone https://github.com/patrickleweryharris/pintools.git
$ cd pintools
$ make install
```

### Dependencies

See [requirements.txt](requirements.txt)

## Usage

### Pinboard Authentication

Pintools uses [lionheart/pinboard.py](https://github.com/lionheart/pinboard.py)
to connect with Pinboard. Authentication is completed using your Pinboard API
token, which can be found in [settings->password](https://pinboard.in/settings/password) on Pinboard.

Pintools will by default look for your Pinboard API token in `$PINBOARD_API_TOKEN`. Alternatively it
can be specified using the `--pinboard_token` argument if you do not want to use
the environment variable.

### Sync Github Stars

Pintools can be used to copy Github stars to your Pinboard account. Starred
gists are not currently copied.

Usage:
```
pintools github [-h] [--token TOKEN]
```

#### Github Authentication

Pintools uses [PyGithub](https://github.com/PyGithub/PyGithub) to connect to
Github. In order to authenticate with Github, you will need to create a [Personal
Access Token](https://github.com/settings/tokens) in your Github account, with the
`read:user` scope.

Pintools will look for this Personal Access Token in `$PYGITHUB_ACCESS_TOKEN`.
Alternatively, this token can be specified using the `--token` arguement

### Sync Reddit Saved Links
Pintools can be used to copy Reddit saved items to your Pinboard account. Note
that new saved items can be saved via [IFTTT](https://ifttt.com), but if you want to
back up the entirety of your saved links, you need to use a script like this
because IFTTT will only work on new saved items.

Saved comments are not currently copied.

Usage:
```
pintools reddit [-h] [--secret SECRET] [--client_id CLIENT_ID] USERNAME PASSWORD
```

#### Reddit Authentication

Pintools uses [PRAW](https://praw.readthedocs.io/en/latest/) to connect with
Reddit. You will need to crate a developer application (personal use script) on
Reddit in order to authenticate. Please follow the PRAW insructions on 'Password
Flow'
[here](https://praw.readthedocs.io/en/latest/getting_started/authentication.html#password-flow).

Once you have created a personal use script application on Reddit, save the
Client-ID and Client-Secret. By default, pintools will look for these in
`$REDDIT_CLIENT_ID` and `$REDDIT_CLIENT_SECRET`. Alternatively, these can be
specified using the `--client_id` and `--secret` arguments. Username and
password for Reddit must also be provided on the command line.

### Organize Pinboard links by originating site

Pintools can be used to tag each bookmark against the originating site,
for easier organization. For example, any bookmark from `github.com` will
be tagged with `github`.

Usage:
```
pintools tags [-h] [--config CONFIG_FILE]
```
This can be optionally customized using a config file. The config file can group several
domains under one URL.

The config file uses YAML syntax like so:
```
domains: # list title must always be 'domains'
  utoronto: # Each key is the final tag you want on your bookmarks
    - utoronto # each item in the list is the base URL you want the tag associated with
    - cs.toronto # don't include .com or www.
  twitter:
    - t
    - twitter
```
There is an example config file [here](domain_assoc.yml)

### Fix Titles
Pintools can fix bookmark titles for you, which sometimes get messed up when
saving bookmarks automatically with IFTTT.

Usage:
```
pintools titles [-h] [--tag TAG]
```
In order to prevent accidentally nuking all your bookmark titles, this feature
operates on a single tag. For each bookmark with the tag specified, pintools
will grab the title of the URL, and update the bookmark's title in Pinboard.
