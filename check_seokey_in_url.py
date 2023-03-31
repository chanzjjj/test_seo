'''检查文档中的seo_key是否都有在线上的url中'''

import xlrd

excel = xlrd.open_workbook('url_files.xlsx') # 读取excel表
sheet = excel.sheet_by_name("Table") # 读取名为“Table”的sheet
norws = sheet.nrows # 总的url数

with open("seo_key.txt", "r", encoding="UTF-8") as fp:
    data = fp.read()
    data = data.split("\n\n")

seo_key_list = []
error_seo_key = []
for i in range(norws):
    url = sheet.cell(i,0).value
    # 过滤tag、商圈、街道聚合页
    if "-popular-restaurants" in url or "popular-restaurants-near-me" in url or "yakinlarindaki-restoranlar" in url or "restoranlar-yorumları" in url:
        continue
    seo_key = url.split("/")[-2]
    # 过滤城市页
    if "tr-tr-" in seo_key:
        continue
    # 如果是店铺图片页、菜单页、评论页，取倒数第3个位置为seo_key
    if seo_key == "fotoğraflar" or seo_key ==  "menüler" or seo_key == "yorum":
        seo_key = url.split("/")[-3]
    # print(seo_key)
    seo_key_list.append(seo_key)

for i in data:
    if i not in seo_key_list:
        error_seo_key.append(i)
print("文档中有但线上url没有的seo_key：%s" % error_seo_key)

