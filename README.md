![GitHub](https://img.shields.io/github/license/educollado/rss_podcast_generator)
![GitHub last commit](https://img.shields.io/github/last-commit/educollado/rss_podcast_generator)
![GitHub repo size](https://img.shields.io/github/repo-size/educollado/rss_podcast_generator)
![Twitter Follow](https://img.shields.io/twitter/follow/ecollado)
![Mastodon Follow](https://img.shields.io/mastodon/follow/72314?domain=https%3A%2F%2Fmastodon.social&style=social)
# rss_podcast_generator
Script to generate a podcast feed for static sites.

## How it works
You have 2 directories with yaml files: 
* channel.yaml
* items/
    * item.yaml
    * item2.yaml
    * something.yaml

In channel.yaml you define generic data from your podcast's feed:

In all yaml files inside folder items you can write everything you need, one file per chapter.
The name of the file is not important but you need the file to end in .yaml.

To work after fill the configuration files simple:

```bash
python rssgenerator.py
```

To install dependencies I suggest to use:

```bash
pip install -r requirements.txt
```

## The output

In output folder you have the file podcast.rss, this is your feed and now you can upload where you need it.

## License
[GPL3](https://github.com/educollado/rss_podcast_generator/blob/main/LICENSE)
