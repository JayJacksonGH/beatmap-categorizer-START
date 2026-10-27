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
        #print(store.x, store.y, store.time, store.type, store.sliderParam)
        hitobjects.append(store)

twohitobjects = []
class twoobjectvalues:
    def __init__(self, x1, y1, x2, y2, time1, time2):
        dx = int(x2)-int(x1)
        dy = int(y2)-int(y1)
        self.distance = math.sqrt((dx)**2 + (dy)**2)
        self.deltatime = int(time2) - int(time1)
        self.angle = math.degrees(math.atan2(dy, dx))
        self.dx = abs(dx)
        self.dy = abs(dy)
        if self.deltatime > 0:
            self.speed = self.distance / self.deltatime
        else:
            self.speed = 0

test = twoobjectvalues(hitobjects[0].x, hitobjects[0].y, hitobjects[1].x, hitobjects[1].y, hitobjects[0].time, hitobjects[1].time)
print(test.distance, test.deltatime, test.angle, test.dx, test.dy, test.speed)