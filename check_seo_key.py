import re


'''匹配是否只包含英文字母、数字以及-，不是的话打印出来'''
len_seokey = 0
with open("seo_key.txt", "r", encoding="UTF-8") as fp:
    data = fp.read()
    data = data.split("\n")
    # print(data)
    error_seo_key = []
    for i in data:
        if re.match(r'^[A-Za-z0-9-]+$', i):
            len_seokey += 1
            continue
        else:
            error_seo_key.append(i)
    # print(error_seo_key)
    if len(error_seo_key) == 0:
        print("seo_key没问题，运行的seo_key数量：%s" % len_seokey)
    else:
        print("有问题的seo_key：%s" % error_seo_key)



