# rss_podcast_generator
Script to generate a podcast feed for static sites.

# How it works
You have 2 directories with yaml files: 
* channel.yaml
* items/
    * item.yaml
    * item2.yaml
    * something.yaml

In channel.yaml you define generic data from your podcast's feed:

In all yaml files inside folder items you can write everything you need, one file per chapter.
The name of the fale is not importart but you need the file to end in .yaml.

To work after fill the configuration files simple:

python rssgenerator.py


To install dependencies I suggest to use:

pip install -r requirements.txt

# The output

In output folder you have the file podcast.rss, this is your feed and now you can upload where you need it.
