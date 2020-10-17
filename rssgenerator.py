from read_channel import generate_channel
from read_items import generate_items
from time import gmtime, strftime

channel=generate_channel()
items=generate_items()
file='output/podcast.rss'

filehandle = open(file, 'w')

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

filehandle.write('\n	<atom:link rel="hub" href="https://pubsubhubbub.appspot.com/" />')
filehandle.write('\n	<itunes:summary>{}</itunes:summary>'.format(channel['itunes']['summary']))
filehandle.write('\n	<itunes:author>{}</itunes:author>'.format(channel['itunes']['author']))
filehandle.write('\n	<itunes:explicit>{}</itunes:explicit>'.format(channel['itunes']['explicit']))
filehandle.write('\n	<itunes:image href="{}" />'.format(channel['itunes']['image']))
filehandle.write('\n	<itunes:type>{}</itunes:type>'.format(channel['itunes']['type']))
filehandle.write('\n	<itunes:owner>')
filehandle.write('\n		<itunes:name>{}</itunes:name>'.format(channel['itunes']['owner']['name']))
filehandle.write('\n		<itunes:email>{}</itunes:email>'.format(channel['itunes']['owner']['email']))
filehandle.write('\n	</itunes:owner>')
filehandle.write('\n	<managingEditor>{}</managingEditor>'.format(channel['itunes']['owner']['email']))
filehandle.write('\n	<copyright>{}</copyright>'.format(channel['itunes']['owner']['name']))
filehandle.write('\n	<itunes:subtitle>{}</itunes:subtitle>'.format(channel['itunes']['subtitle']))
filehandle.write('\n	<image>')
filehandle.write('\n		<title>{}</title>'.format(channel['title']))
filehandle.write('\n		<url>{}</url>'.format(channel['itunes']['image']))
filehandle.write('\n		<link>{}</link>'.format(channel['web_link']))
filehandle.write('\n	</image>')
for channel_category in channel['itunes']['categories']:
	filehandle.write('\n	<itunes:category text="{}" />'.format(channel_category))¡
filehandle.write('\n	<googleplay:category text="{}"/>'.format(channel['itunes']['categories'][0]))
filehandle.write('\n	<rawvoice:rating>{}</rawvoice:rating>'.format(channel['rating']))
filehandle.write('\n	<rawvoice:location>{}</rawvoice:location>'.format(channel['location']))
filehandle.write('\n	<rawvoice:frequency>{}</rawvoice:frequency>'.format(channel['frequency']))
filehandle.write('\n<rawvoice:subscribe feed="{}" itunes="{}" tunein="{}" spotify="{}"></rawvoice:subscribe>'.format(channel['subscribe']['feed'],channel['subscribe']['itunes'],channel['subscribe']['tunein'],channel['subscribe']['spotify']))
filehandle.write('\n')
for i in items:
	filehandle.write('\n<item>')
	filehandle.write('\n	<title>{}</title>'.format(i['title']))
	filehandle.write('\n	<link>{}</link>'.format(i['link']))
	filehandle.write('\n	<dc:creator><![CDATA[{}]]></dc:creator>'.format(i['creator']))
	filehandle.write('\n	<pubDate>{}</pubDate>'.format(i['pubDate']))
	for audio_category in i['categories']:
		filehandle.write('\n	<category><![CDATA[{}]]></category>'.format(audio_category))
	filehandle.write('\n	<description><![CDATA[{}]]></description>'.format(i['description']))
	filehandle.write('\n	<content:encoded><![CDATA[{}]]></content:encoded>'.format(i['content']))
	filehandle.write('\n	<enclosure url="{}" length="{}" type="{}" />'.format(i['enclosure'], i['length'], i['type']))
	filehandle.write('\n	<itunes:subtitle>{}</itunes:subtitle>'.format(i['itunes']['subtitle']))
	filehandle.write('\n	<itunes:summary><![CDATA[{}]]></itunes:summary>'.format(i['itunes']['summary']))
	filehandle.write('\n	<itunes:author>{}</itunes:author>'.format(i['itunes']['author']))
	filehandle.write('\n	<itunes:duration>{}</itunes:duration>'.format(i['itunes']['duration']))
	filehandle.write('\n</item>')
filehandle.write('\n\n</channel>')
filehandle.write('\n</rss>')
filehandle.close()


