import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/72.0.3626.109 Safari/537.36'}

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


items = parser_anime(base_url, headers)

for item in items:
    print(item)
