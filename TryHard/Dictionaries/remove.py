thisDic = {
    "name" : "kkk",
    "color" : "red",
    "nn" : "bb",
    "year" : 1999
}

thisDic.pop("nn")
# del thisDic["name"] có thể sử dụng del để xoá
# del thisDic nếu sử dụng sẽ gặp lỗi vì sẽ xoá hết
#thisDic.clear() sẽ xoá toàn bộ trả về {}
print(thisDic) #remove {"nn":"bb"}

thisDic.popitem()#xoa cai cuoi cung
print(thisDic)