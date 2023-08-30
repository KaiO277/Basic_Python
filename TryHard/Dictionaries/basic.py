thisDic = {
    "name" : "kkk",
    "color" : "red",
    "nn" : "bb"
}
print(thisDic["name"])
print(thisDic.get("name"))
print(thisDic.keys())
print(thisDic.values())
print(len(thisDic))
print(type(thisDic))
for x in thisDic.values():
    print(x)

for i in thisDic.keys():
    print(i)    