import urllib.request
import math
mapid = "890326"
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

print(hitobjects[0].sliderParam)