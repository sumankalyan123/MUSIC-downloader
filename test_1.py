import requests
from bs4 import BeautifulSoup
import urllib.request
import random
import glob, os, shutil
from urllib import parse


def get_all_download_links(song_link_from_google):
    download_links = []
    for url in song_link_from_google:
        #print (url)
        source_code = requests.get(url, allow_redirects=False)
        #print (source_code)
        plain_text = source_code.text.encode('ascii', 'replace')
        #print (plain_text)
        soup = BeautifulSoup(plain_text, 'html.parser')
        #print (soup)
        for link in soup.find_all("a"):
            href = link.get('href')
            #print (href)
            href = str(href)
            if href.endswith('.mp3') or href[-4:] is '.mp3':
                download_links.append(href)
    return download_links


test = ['https://raagtune.com/song/hu3l1fw8/Nimbooda_Nimbooda.html', 'https://mp3mad.com/download-227090/Nimbooda-Nimbooda-Various.html', 'https://mymp3singer.site/download/9082/04_-_nimbooda_nimbooda', 'http://emomp3song.com/download/1115/nimbooda_nimbooda', 'http://mymp3song.org/filedownload/3288/nimbooda_nimbooda', 'http://gaana.com/song/albela-sajan', 'http://wapking.live/fileDownload/97419/nimbooda_nimbooda.html', 'https://mp3mad.net/data/song/235571/nimbooda-various.html', 'https://www.youtube.com/watch?v=YJzT1KMjQ0k', 'http://raagtune.tv/brymv/download-NIMBOODA-mp3.html']
name = get_all_download_links(test)
print (name)