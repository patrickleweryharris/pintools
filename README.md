# pinboard
Scripts for importing links from various services to Pinboard (https://pinboard.in)

## Table of Contents
* [Install](#install)
* [Usage](#usage)
* [todo](#todo)

## Install

todo

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

```
pintools reddit [-h] [--secret SECRET] [--client_id CLIENT_ID] USERNAME PASSWORD
```

#### Reddit Authentication

todo

### Organize Pinboard links by originating site

todo

## TODO

- [x] Add functionality to save Reddit saved links to Pinboard
- [x] Add functionality to save Github stars to Pinboard
- [ ] Port pin-tags script to pintools
- [ ] Pypi upload
- [ ] Automate Pypi uploads on releases with Github actions
- [ ] Readme
