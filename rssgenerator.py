#!/usr/bin/env python3

from read_channel import generate_channel
from read_items import generate_items
from time import gmtime, strftime


def main():
    channel = generate_channel()
    items = generate_items()
    file = 'output/podcast.rss'

    with open(file, 'w') as filehandle:
        filehandle.write('''<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"
	xmlns:content="http://purl.org/rss/1.0/modules/content/"
	xmlns:wfw="http://wellformedweb.org/CommentAPI/"
	xmlns:dc="http://purl.org/dc/elements/1.1/"
	xmlns:atom="http://www.w3.org/2005/Atom"
	xmlns:sy="http://purl.org/rss/1.0/modules/syndication/"
	xmlns:slash="http://purl.org/rss/1.0/modules/slash/"
	xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
	xmlns:rawvoice="http://www.rawvoice.com/rawvoiceRssModule/"
	xmlns:googleplay="http://www.google.com/schemas/play-podcasts/1.0"
	xmlns:georss="http://www.georss.org/georss"
	xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">

<channel>''')
        filehandle.write('\n<title>{}</title>'.format(channel['title']))
        filehandle.write('\n<atom:link href="{}" rel="self" type="application/rss+xml" />'.format(channel['feed_link']))
        filehandle.write('\n<link>{}</link>'.format(channel['web_link']))
        filehandle.write('\n<description>{}</description>'.format(channel['description']))
        filehandle.write('\n<lastBuildDate>{}</lastBuildDate>'.format(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())))
        filehandle.write('\n<language>{}</language>'.format(channel['language']))

        filehandle.write('\n\t<atom:link rel="hub" href="https://pubsubhubbub.appspot.com/" />')
        filehandle.write('\n\t<itunes:summary>{}</itunes:summary>'.format(channel['itunes']['summary']))
        filehandle.write('\n\t<itunes:author>{}</itunes:author>'.format(channel['itunes']['author']))
        filehandle.write('\n\t<itunes:explicit>{}</itunes:explicit>'.format(channel['itunes']['explicit']))
        filehandle.write('\n\t<itunes:image href="{}" />'.format(channel['itunes']['image']))
        filehandle.write('\n\t<itunes:type>{}</itunes:type>'.format(channel['itunes']['type']))
        filehandle.write('\n\t<itunes:owner>')
        filehandle.write('\n\t\t<itunes:name>{}</itunes:name>'.format(channel['itunes']['owner']['name']))
        filehandle.write('\n\t\t<itunes:email>{}</itunes:email>'.format(channel['itunes']['owner']['email']))
        filehandle.write('\n\t</itunes:owner>')
        filehandle.write('\n\t<managingEditor>{} ({})</managingEditor>'.format(channel['itunes']['owner']['email'], channel['itunes']['owner']['name']))
        filehandle.write('\n\t<copyright>{}</copyright>'.format(channel['itunes']['owner']['name']))
        filehandle.write('\n\t<itunes:subtitle>{}</itunes:subtitle>'.format(channel['itunes']['subtitle']))
        filehandle.write('\n\t<image>')
        filehandle.write('\n\t\t<title>{}</title>'.format(channel['title']))
        filehandle.write('\n\t\t<url>{}</url>'.format(channel['itunes']['image']))
        filehandle.write('\n\t\t<link>{}</link>'.format(channel['web_link']))
        filehandle.write('\n\t</image>')
        for channel_category in channel['itunes']['categories']:
            filehandle.write('\n\t<itunes:category text="{}" />'.format(channel_category))
        filehandle.write('\n\t<googleplay:category text="{}"/>'.format(channel['itunes']['categories'][0]))
        filehandle.write('\n\t<rawvoice:rating>{}</rawvoice:rating>'.format(channel['rating']))
        filehandle.write('\n\t<rawvoice:location>{}</rawvoice:location>'.format(channel['location']))
        filehandle.write('\n\t<rawvoice:frequency>{}</rawvoice:frequency>'.format(channel['frequency']))
        filehandle.write('\n<rawvoice:subscribe feed="{}" itunes="{}" tunein="{}" spotify="{}"></rawvoice:subscribe>'.format(
            channel['subscribe']['feed'], channel['subscribe']['itunes'],
            channel['subscribe']['tunein'], channel['subscribe']['spotify']))
        filehandle.write('\n')
        for i in items:
            filehandle.write('\n<item>')
            filehandle.write('\n\t<title>{}</title>'.format(i['title']))
            filehandle.write('\n\t<link>{}</link>'.format(i['link']))
            filehandle.write('\n\t<dc:creator><![CDATA[{}]]></dc:creator>'.format(i['creator']))
            filehandle.write('\n\t<pubDate>{}</pubDate>'.format(i['pubDate']))
            for audio_category in i['categories']:
                filehandle.write('\n\t<category><![CDATA[{}]]></category>'.format(audio_category))
            filehandle.write('\n\t<description><![CDATA[{}]]></description>'.format(i['description']))
            filehandle.write('\n\t<content:encoded><![CDATA[{}]]></content:encoded>'.format(i['content']))
            filehandle.write('\n\t<enclosure url="{}" length="{}" type="{}" />'.format(i['enclosure'], i['length'], i['type']))
            filehandle.write('\n\t<itunes:subtitle>{}</itunes:subtitle>'.format(i['itunes']['subtitle']))
            filehandle.write('\n\t<itunes:summary><![CDATA[{}]]></itunes:summary>'.format(i['itunes']['summary']))
            filehandle.write('\n\t<itunes:author>{}</itunes:author>'.format(i['itunes']['author']))
            filehandle.write('\n\t<itunes:duration>{}</itunes:duration>'.format(i['itunes']['duration']))
            filehandle.write('\n</item>')
        filehandle.write('\n\n</channel>')
        filehandle.write('\n</rss>')


if __name__ == '__main__':
    main()
