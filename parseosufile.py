import urllib.request
import math
mapid = "5949203"
map = urllib.request.urlopen("https://osu.ppy.sh/osu/" + mapid).read().decode("utf-8")
osumaptext = map.split("[HitObjects]")[1].split("\n")

class hitobjectdifference:
    def __init__

osuobject = osumaptext[1].split(",")
x = int(osuobject[0])
y = int(osuobject[1])
time = int(osuobject[2])
objecttype = format(int(osuobject[3]), "08b")

