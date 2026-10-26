import urllib.request
mapid = "5949203"
map = urllib.request.urlopen("https://osu.ppy.sh/osu/" + mapid).read().decode("utf-8")
osumaptext = map.split("[HitObjects]")[1].split("\n")
print(repr(osumaptext[1]))
print(repr(osumaptext[-1]))


