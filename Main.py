import urllib.request
import lxml.html
import os
import random


def write_all_download_links(song_link_from_google):
    for google_link in song_link_from_google:
        #os.remove("links.tmp")
        connection = urllib.request.urlopen(song_link_from_google)
        dom =  lxml.html.fromstring(connection.read())
        for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
                 if link.endswith(('.mp3')) :
                    with open("links.tmp", "a") as myfile:
                        myfile.write(link +' '+"\n")

def read_from_temp_file():
    songs=[]
    names_with_download_tag = []
    for line in open('links.tmp','r').readlines():
        songs.append(line.strip('.mp3'))
        return songs

def download_web_image(url):
    for song in url :
        name = random.randrange(1, 1000000)
        full_name = str(name) + ".mp3"
        urllib.request.urlretrieve(song, full_name)

url = 'http://mr-jatt.com/download-us/jaadu-teri-nazar-udit-narayan.html'
write_all_download_links(url)
name = []
name = read_from_temp_file()
print (name[:])
download_web_image(name)