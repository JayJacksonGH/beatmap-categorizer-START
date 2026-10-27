import urllib.request
import math
mapid = "5949203"
map = urllib.request.urlopen("https://osu.ppy.sh/osu/" + mapid).read().decode("utf-8")
osumaptext = map.split("[HitObjects]")[1].split("\n")

class hitobjectdifference:
    def __init__(self, x1, y1, x2, y2, time1, time2, type1, type2):
        self.distance = math.sqrt((int(x1)-int(x2))**2 + (int(y1)-int(y2))**2)
        self.timediff = int(time2) - int(time1)
test = hitobjectdifference(1, 1, 2, 2, 1000, 2000, 1, 1)
print(test.distance)
osuobject = osumaptext[1].split(",")
x = int(osuobject[0])
y = int(osuobject[1])
time = int(osuobject[2])
objecttype = format(int(osuobject[3]), "08b")

