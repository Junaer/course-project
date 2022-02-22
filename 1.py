import requests
import json
from tqdm import tqdm

class vk_api():

    def __init__(self):
        pass

    token_vk = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
    id_vk = input('Укажите id в Вконтакте - ')
    params = {
        'owner_id': id_vk,
        'album_id': 'profile',
        'extended': '1',
        'photo_sizes': '1',
        'access_token': token_vk,
        'v': '5.131'
    }
    URL = 'https://api.vk.com/method/photos.get'

    def get_max_size_photos_url(self):
        count = 0
        res = requests.get(self.URL, params=self.params)
        sizes = res.json()['response']['items']
        size = []
        max_size = []
        for s in tqdm(sizes):
            count +=1
            if count == 6:
                break
            size.append(s['sizes'])
        for si in size:
            max_size.append(si[5]['url'])
        return max_size

    def get_like_name(self):
        count = 0
        res = requests.get(self.URL, params=self.params)
        likes = (res.json()['response']['items'])
        name = []
        for like in tqdm(likes):
            count += 1
            if count == 6:
                break
            elif str(like['likes']['count']) in name:
                l = str(like['likes']['count'])+'date'+str(like['date'])
                name.append(l)
            else:
                l = str(like['likes']['count'])
                name.append(l)
        return name

vk = vk_api()

class yandex:
    token = input('Укажите токен своего яндекс диска - ')
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': '{}'.format(f'{token}')
    }

    def __init__(self):\
        pass


    def get_folder(self):
        params = {
            'path': 'vk'
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=self.headers, params=params)
        response.json()

    def download_file_for_url(self, url, path):
        yan.get_folder()
        data2 = []
        for ur, pat in tqdm(zip(url, path)):
                params = {
                    'url': ur,
                    'path': f'vk/{pat}'
                }
                response = requests.post('https://cloud-api.yandex.net/v1/disk/resources/upload', headers=self.headers, params=params)
                data = [{
                    'file_name': pat,
                    'size': 'w'
                }]
                data2.append(data)
                with open('sample.json', 'w') as f:
                    json.dump(data2, f, ensure_ascii=False, indent=2)
        return print('Cкачивание завершино')

yan = yandex()
yan.download_file_for_url(vk.get_max_size_photos_url(), vk.get_like_name())




















