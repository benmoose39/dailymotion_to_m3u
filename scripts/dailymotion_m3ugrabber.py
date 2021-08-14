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
import sys

proxies = {}
if len(sys.argv) == 2:
    proxies = {
                'http' : sys.argv[1],
                'https' : sys.argv[1]
              }

na = 'https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u'
def grab(line):
    try:
        _id = line.split('/')[4]
        response = s.get(f'https://www.dailymotion.com/player/metadata/video/{_id}', proxies=proxies).json()['qualities']['auto'][0]['url']
        m3u = s.get(response, proxies=proxies).text
        m3u = m3u.strip().split('\n')[1:]
        d = {}
        cnd = True
        for item in m3u:
            if cnd:
                resolution = item.strip().split(',')[2].split('=')[1]
                if resolution not in d:
                    d[resolution] = []
            else:
                d[resolution]= item
            cnd = not cnd
        #print(m3u)
        m3u = d[max(d, key=int)]    
    except Exception as e:
        m3u = na
    finally:
        print(m3u)

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
            grab(line)
        
