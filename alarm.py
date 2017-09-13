import urllib2
from xml.etree import ElementTree as etree
import datetime as dt
import time
import calendar
import webbrowser

while(dt.datetime.now().hour != 13):
    print("Not time yet...")
    time.sleep(60)

# Get the current day
my_date = dt.date.today()
today = calendar.day_name[my_date.weekday()]

#Parse XML
file = urllib2.urlopen('https://www.npr.org/rss/podcast.php?id=510318')
#convert to string:
data = file.read()
#close file because we dont need it anymore:
file.close()

# Find the current date and open the url
root = etree.fromstring(data)
for item in root.findall('channel/item'):
    title = item.find('title').text
    if today in title:
        print item.find('enclosure').attrib['url']
        webbrowser.open(item.find('enclosure').attrib['url'])

