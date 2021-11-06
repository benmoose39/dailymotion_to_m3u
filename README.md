<h1 align="center"> Dailymotion_to_m3u </h1>

[![M3U generator for Dailymotion](https://github.com/benmoose39/dailymotion_to_m3u/actions/workflows/grabber.yml/badge.svg)](https://github.com/benmoose39/dailymotion_to_m3u/actions/workflows/grabber.yml)

`https://raw.githubusercontent.com/benmoose39/dailymotion_to_m3u/main/dailymotion-{PREFERRED SERVER}.m3u`
m3u links of Dailymotion live channels, auto-updated everyday.

### Usage
Paste one of the following URL based on your location, to avoid buffering: 

`https://raw.githubusercontent.com/benmoose39/dailymotion_to_m3u/main/dailymotion-US.m3u`

`https://raw.githubusercontent.com/benmoose39/dailymotion_to_m3u/main/dailymotion-EU.m3u`

`https://raw.githubusercontent.com/benmoose39/dailymotion_to_m3u/main/dailymotion-SG.m3u`

### Run the tool on your local machine
``` bash
git clone https://github.com/benmoose39/dailymotion_to_m3u.git
cd dailymotion_to_m3u
chmod +x autorun.sh
./autorun.sh
```

### Use proxy to grab m3u
`python3 dailymotion_m3ugrabber.py <proxy_server_ip:port>`

eg: `python3 dailymotion_m3ugrabber.py 192.168.13.13:1337`

### Add more channels
Connect on discord and request new channels or create a pull request

If running locally, edit `dailymotion_channel_info.txt` to add more dailymotion channels.

Connect: https://discord.gg/dmgYmAEdee


### Support

🙂 https://www.buymeacoffee.com/benmoose39
