from zipfile import ZipFile
import os
import re
# with ZipFile(r"D:\일.zip") as obj_zip:
#     Filenames=obj_zip.namelist()
#     for name in Filenames:
#         if name[0]=="r":
#             obj_zip.extract(name,r"D:")


# with ZipFile(r"D:\2018.zip") as obj_zip:
#     Filenames=obj_zip.namelist()
#     print(obj_zip.infolist())
#     input()
#     for name in Filenames:
#         # print(re.findall("[\w]*RKSI[\w]*",name))
#         print(name)
#         input()

#         # if re.findall("[\w]*RKSI[\w]*",name):
#         #     obj_zip.extract(name,r"D:")


zf=ZipFile(r"D:/2018.zip")

# zf.extractall("D:/")
# print(zf.compression) # 뭔지 모르겠음... 암튼 0 나옴
for i in zf.infolist(): # 됐다..! , huge사이즈라.. DL 디스크100% 사용량이 뜸!
    if re.match(r"^2018/RKSI/[\w]*",i.filename):
        zf.extract(i,"D:")
        print(i.filename)
# for name in 
zf.close()
