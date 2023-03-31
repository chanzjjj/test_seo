'''检查是否有重复的url'''

import xlrd

excel = xlrd.open_workbook('0315_01.xlsx') # 读取excel表
sheet = excel.sheet_by_name("Table") # 读取名为“Table”的sheet
norws = sheet.nrows # 总的url数

url_list = []
for i in range(norws):
    url = sheet.cell(i,0).value
    url_list.append(url)

set_url_list = set(url_list)
error_url_list = []
if len(set_url_list) != len(url_list):
    print("有重复的url")
    for i in set_url_list:
        url_count = url_list.count(i)
        # print(url_count)
        if url_count > 1:
            error_url_list.append(i)
    print("重复的url：%s" % error_url_list)
else:
    print("无重复的url")

