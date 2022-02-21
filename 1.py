import requests
import json
from pprint import pprint
from tqdm import tqdm

class vk_api():
    def __init__(self):
        pass

    token_vk = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
    URL = 'https://api.vk.com/method/photos.get'

    def get_max_size_photos_url(self, id_vk):
        params = {
            'owner_id': id_vk,
            'album_id': 'profile',
            'extended': '1',
            'photo_sizes': '1',
            'access_token': self.token_vk,
            'v': '5.131'
        }
        count = 0
        res = requests.get(self.URL, params=params)
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

    def get_like_name(self, id_vk):
        params = {
            'owner_id': id_vk,
            'album_id': 'profile',
            'extended': '1',
            'photo_sizes': '1',
            'access_token': self.token_vk,
            'v': '5.131'
        }
        count = 0
        res = requests.get(self.URL, params=params)
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
    def __init__(self):
        pass

    def get_folder(self, token):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': '{}'.format(token)
        }
        params = {
            'path': 'vk'
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=headers, params=params)
        response.json()

    def download_file_for_url(self, url, path, token):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': '{}'.format(token)
        }
        data2 = []
        for ur, pat in tqdm(zip(url, path)):
                params = {
                    'url': ur,
                    'path': f'vk/{pat}'
                }
                response = requests.post('https://cloud-api.yandex.net/v1/disk/resources/upload', headers=headers, params=params)
                data = [{
                    'file_name': pat,
                    'size': 'w'
                }]
                data2.append(data)
                with open('sample.json', 'w') as f:
                    json.dump(data2, f, ensure_ascii=False, indent=2)
        return print('Cкачивание завершино')

class save_foto(vk_api,yandex):
    def __init__(self):
        pass

    def programm(self, id, token):
        yan = yandex()
        yan.get_folder(token)
        yan.download_file_for_url(vk.get_max_size_photos_url(id), vk.get_like_name(id), token)

start = save_foto()
start.programm('492994968', '')
















