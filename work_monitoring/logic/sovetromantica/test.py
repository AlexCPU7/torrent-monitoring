import requests

def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

print(is_downloadable('https://www.youtube.com/watch?v=9bZkp7q19f0'))
# >> False
print(is_downloadable('http://google.com/favicon.ico'))
print(is_downloadable('https://sovetromantica.com/anime/695-dororo/episode_9-subtitles'))
# >> True
import requests

url = 'https://sc7.sovetromantica.com/anime/695_dororo/episodes/subtitles/episode_10.mp4'
r = requests.get(url, allow_redirects=True)
open('episode_10.mp4', 'wb').write(r.content)

print('FINISH')