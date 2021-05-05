import os
import yaml

with open(r'spotify_streams.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)
    for stream in config["streams"]:
        os.system(f'./SpotifyCreate.sh -t {stream["title"]} -f {stream["folder"]} -c {stream["cardid"]} -s {stream["spotify"]}')
