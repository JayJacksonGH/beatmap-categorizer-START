import urllib.request
import math
mapid = "5265850"
map = urllib.request.urlopen("https://osu.ppy.sh/osu/" + mapid).read().decode("utf-8")
osumaptext = map.split("[HitObjects]")[1].split("\n")

class hitobject:
    def __init__(self, x, y, time, type, sliderParam):
        self.x = x
        self.y = y
        self.time = time
        self.type = type
        if any(l in sliderParam for l in ["B", "C", "L", "P"]):
            self.sliderParam = sliderParam
        else:
            self.sliderParam = None

hitObjectTypes = {
    0: "circle",
    1: "slider",
    3: "spinner",
}
hitobjects = []
for i, line in enumerate(osumaptext):
    osuobject = osumaptext[i].split(",")
    if line.strip():
        objecttype = format(int(osuobject[3]), "08b")
        objecttype = int(objecttype)
        if objecttype & 1:
            objecttype = hitObjectTypes[0]
        elif objecttype & 2:
            objecttype = hitObjectTypes[1]
        elif objecttype & 8:
            objecttype = hitObjectTypes[3]
        store = hitobject(osuobject[0], osuobject[1], osuobject[2], objecttype, osuobject[5]) 
        print(store.x, store.y, store.time, store.type, store.sliderParam)
        hitobjects.append(store)


class parameters:
    def __init__(self, x1, y1, x2, y2, time1, time2):
        self.distance = math.sqrt((int(x1)-int(x2))^2 + (int(y1)-int(y2))^2)
        self.deltatime = int(time2) - int(time1)

test = parameters(hitobjects[0].x, hitobjects[0].y, hitobjects[1].x, hitobjects[1].y, hitobjects[0].time, hitobjects[1].time)
print(test.distance, test.deltatime)