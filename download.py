import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".mp3"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://dl.jatt.link/lq.jatt.link/cdn8/ab0c2fa153112489c0c97b7598089d2b/kdhmv/Channa Mereya-(Mr-Jatt.com).mp3")