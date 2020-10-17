# RSS Podcast Generator
![GitHub](https://img.shields.io/github/license/educollado/rss_podcast_generator)
![GitHub last commit](https://img.shields.io/github/last-commit/educollado/rss_podcast_generator)
![GitHub repo size](https://img.shields.io/github/repo-size/educollado/rss_podcast_generator)
![Twitter Follow](https://img.shields.io/twitter/follow/ecollado)
![Mastodon Follow](https://img.shields.io/mastodon/follow/72314?domain=https%3A%2F%2Fmastodon.social&style=social)

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

## Configuration Files

Note: Now you can define as many categories as you want, but iTunes uses 3

example of configuration files:

### channel.yaml (this name is forced)
```yaml
title: A Ratos Podcast
feed_link: https://mysuperpodcast.com/podcast.rss
web_link: https://mysuperpodcast.com
description: Description of my podcast
language: es
itunes:
  subtitle: iTunes subtitle for my podcast
  summary: iTunes podcast summary
  author: John Doe
  explicit: clean
  image: http://mysuperpodcast.com/image1600x1600.jpg
  type: episodic
  owner:
    name: John Doe
    email: podcast@mysuperpodcast.com
  categories:
    - Technology
    - News
    - Education
copyright: John Doe
rating: TV-Y
location: Madrid, Spain
frequency: weekly
subscribe:
  feed: https://mysuperpodcast.com/podcast.rss
  itunes: 
  tunein: 
  spotify: 

```

### item.yaml (any name ended in .yaml in /items folder)
```yaml
title: My super chapter
link: https://misuperchapter.com/chaper1
creator: John Doe
pubDate: Fri, 31 Dec 1999 23:59:59 EST
categories:
  - Tehcnology
  - News
  - Education
description: Chapter description
content: Chapter content
enclosure: https://misuperchapter.com/chaper1.mp3
length: 207310
type: audio/mpeg
itunes:
  subtitle: iTunes chapter subtitle
  summary: iTunes chapter summary
  author: John Doe
  duration: 29:14
```
## License
[GPL3](https://github.com/educollado/rss_podcast_generator/blob/main/LICENSE)
