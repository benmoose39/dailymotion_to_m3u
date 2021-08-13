#! /usr/bin/python3

banner = r'''
#########################################################################
#      ____            _           _   __  __                           #
#     |  _ \ _ __ ___ (_) ___  ___| |_|  \/  | ___   ___  ___  ___      #
#     | |_) | '__/ _ \| |/ _ \/ __| __| |\/| |/ _ \ / _ \/ __|/ _ \     #
#     |  __/| | | (_) | |  __/ (__| |_| |  | | (_) | (_) \__ \  __/     #
#     |_|   |_|  \___// |\___|\___|\__|_|  |_|\___/ \___/|___/\___|     #
#                   |__/                                                #
#                                  >> https://github.com/benmoose39     #
#########################################################################
'''

import requests
import os

na = 'https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u'
gh_basem3u = 'https://raw.githubusercontent.com/benmoose39/dailymotion_to_m3u/main/ch/'

def grab(line, ch_name):
    try:
        os.chdir('ch')
        _id = line.split('/')[4]
        response = s.get(f'https://www.dailymotion.com/player/metadata/video/{_id}').json()['qualities']['auto'][0]['url']
        m3u = s.get(response).text
    except:
        m3u = na
    finally:
        with open (f'{ch_name}.m3u', 'w') as channel:
            channel.write(m3u)
        os.chdir('../')

print('#EXTM3U')
print(banner)
s = requests.Session()
with open('../dailymotion_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line, ch_name)
            print(f'{gh_basem3u}{ch_name.replace(" ", "%20")}.m3u')
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
