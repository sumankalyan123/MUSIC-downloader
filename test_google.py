import requests
from bs4 import BeautifulSoup
import urllib.request
import random
import glob, os, shutil
from urllib import parse




def read_from_text_file():
    filename = 'names.txt'
    songs = []
    names_with_download_tag = []
    for line in open(filename, 'r').readlines():
        songs.append(line.strip())
        names_with_download_tag = [x + '  mp3 free download ' for x in songs]
    return names_with_download_tag


def search_google(songname):
    url = 'https://www.google.co.in/search?q=' + songname
    source_code = requests.get(url, allow_redirects=False, headers={'User-Agent': 'Mozilla/5.0'})
    plain_text = str(source_code.text.encode('ascii', 'replace'))
    plain_text = plain_text.replace('/url?q=','')
    soup = BeautifulSoup(plain_text, 'html.parser')
    google_search_url_list = []
    for link in  soup.findAll('h3',class_ = 'r'):
        href = str(str(link).replace('<h3 class="r"><a href="',''))
        href_replaced = href[:href.find('&amp;')]
        href_final = parse.unquote(href_replaced)
        google_search_url_list.append(href_final)
    return google_search_url_list

   # return list




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

def download_mp3_song(mp3_download_url):
    for song in reversed(mp3_download_url):
        name = random.randrange(1, 1000000)
        full_name = str(mp3_file_name) + ".mp3"
        if not any(fname == mp3_file_name + '.mp3' for fname in os.listdir(r'C:\Users\sumankalyan\PycharmProjects\MUSIC_DOWNLOADER')):
            urllib.request.urlretrieve(song, full_name)
            print(mp3_file_name + ' Downloaded successfuly')


def check_if_downloaded():
    for File in os.listdir(r'C:\Users\sumankalyan\PycharmProjects\MUSIC_DOWNLOADER'):
        filename = str(File)
        if filename[len(filename)-4:] == '.mp3':
            return 'true'
        else:
            return 'false'

def move_to_backup_dir():
    source_dir = r'C:\Users\sumankalyan\PycharmProjects\MUSIC_DOWNLOADER' #Path where your files are at the moment
    dst = r'C:\Users\sumankalyan\PycharmProjects\MUSIC_DOWNLOADER\BACKUP' #Path you want to move your files to
    files = glob.iglob(os.path.join(source_dir, ".mp3"))
    for file in files:
        if os.path.isfile(file):
            shutil.move(file, dst)


def main_function_call():
    move_to_backup_dir()
    songs_by_user = read_from_text_file()
    print (songs_by_user)
    for user_song in songs_by_user:
        global mp3_file_name
        mp3_file_name = str(user_song[:15]).replace(' ','_')
        google_search_link_list = []
        google_search_link_list = search_google(user_song)
        print (google_search_link_list)
        mp3_download_links_list = get_all_download_links(google_search_link_list)
        print (mp3_download_links_list)
        download_mp3_song(mp3_download_links_list)



main_function_call()






