import os
import requests

from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve

from settings import BASE_DIR

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/72.0.3626.109 Safari/537.36'}

name_site = 'sovetromantica'
site_url = 'https://sovetromantica.com'
base_url = 'https://sovetromantica.com/anime/695-dororo'


def parser_anime(base_url, headers):
    result = None
    session = requests.Session()
    r = session.get(base_url, headers=headers)
    if r.status_code == 200:
        soup = bs(r.content, 'html.parser')
        episodes = soup.find_all('div', attrs={'class': 'episodes-slick_item'})

        result = []
        for episode in episodes:
            name = episode.find('span').text

            find_image = episode.find('a').attrs.get('style')
            image = find_image[22:len(find_image) - 2]

            find_link = episode.find('a',
                                     attrs={'class': 'episodeButtonDownload'}).attrs.get('href')
            link = '{}{}'.format(site_url, find_link)

            result.append({
                'name': name,
                'image': image,
                'link': link
            })
    else:
        print('ERROR')
    return result


# items = parser_anime(base_url, headers)
items = [{'name': 'Эпизод #1',
          'image': 'https://chitoge.sovetromantica.com/anime/695_dororo/images/episode_1_sub.jpg',
          'link': 'https://sc7.sovetromantica.com/anime/695_dororo/episodes/subtitles/episode_10.mp4'},
         {'name': 'Эпизод #2',
          'image': 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png',
          'link': 'https://sc7.sovetromantica.com/anime/695_dororo/episodes/subtitles/episode_10.mp4'}]

save_dir = '{}/media/{}'.format(BASE_DIR, name_site)

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for item in items[:]:
    print(item)

    episode_dir = '{}/{}/'.format(save_dir, item.get('name')).replace(' ', '')
    print(episode_dir)
    if not os.path.exists(episode_dir):
        os.makedirs(episode_dir)

    # save image
    print('STARTING SAVE IMAGE ...')
    url_image = item.get('image')
    destination = episode_dir + url_image.rsplit('/', 1)[1]
    urlretrieve(url_image, destination)
    print('FINISH SAVE IMAGE')

    # save video
    print('STARTING SAVE VIDEO ...')
    url_video = item.get('link')
    destination = episode_dir + url_video.rsplit('/', 1)[1]
    urlretrieve(url=url_video, filename=destination, data=[10])
    print('FINISH SAVE VIDEO')

    print('\n')

    # save video
    # destination = item.get('link').rsplit(episode_dir, 1)[1]
    # urlretrieve(episode_dir, destination)

# img = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png'
#
url = 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png'
url = 'https://sovetromantica.com/download_695_subtitles_1'
print('start')
url = 'https://sc7.sovetromantica.com/anime/695_dororo/episodes/subtitles/episode_10.mp4'
print('start1')
destination = url.rsplit('/', 1)[1]
print(destination)
print('start2')
# urlretrieve(url, destination)
print('stop')


# with open(os.path.join(destination), 'wb') as out_stream:
#     req = requests.get(url + destination, stream=True)
#     for chunk in req.iter_content(1024):  # Куски по 1 КБ
#         out_stream.write(chunk)
