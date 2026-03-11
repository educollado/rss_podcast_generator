# RSS Podcast Generator
![GitHub](https://img.shields.io/github/license/educollado/rss_podcast_generator)
![GitHub last commit](https://img.shields.io/github/last-commit/educollado/rss_podcast_generator)
![GitHub repo size](https://img.shields.io/github/repo-size/educollado/rss_podcast_generator)
![Twitter Follow](https://img.shields.io/twitter/follow/ecollado)
![Mastodon Follow](https://img.shields.io/mastodon/follow/72314?domain=https%3A%2F%2Fmastodon.social&style=social)

Script to generate a podcast feed for static sites.

## Requirements

- Python 3.8+

## Setup

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## How it works

You have 2 directories with yaml files:
* `channel.yaml` — podcast-level metadata
* `items/` — one `.yaml` file per episode
    * `item.yaml`
    * `item2.yaml`
    * `something.yaml`

Fill in the configuration files, then run:

```bash
python rssgenerator.py
```

The generated feed will be written to `output/podcast.rss`.

## Configuration Files

> Note: iTunes uses up to 3 categories, but you can define as many as you want.

### channel.yaml (filename is required)

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

### item.yaml (any name ending in .yaml inside /items)

```yaml
title: My super chapter
link: https://mysuperpodcast.com/chapter1
creator: John Doe
pubDate: Fri, 31 Dec 1999 23:59:59 EST
categories:
  - Technology
  - News
  - Education
description: Chapter description
content: Chapter content
enclosure: https://mysuperpodcast.com/chapter1.mp3
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
