import os
import yaml

with open(r'spotify_streams.yaml') as file:
    config = yaml.load(file)
    for stream in config["streams"]:
        os.system(f'./CreateSpotify.sh --folder {stream["folder"].replace(" ","_")} --item {stream["title"].replace(" ","_")} --spotify {stream["spotify"]} --card {stream["cardid"]}')
