import urllib.request
from bs4 import BeautifulSoup
import re
import xlwt
import xlrd



def read_excel():
    '''读取excel'''
    excel = xlrd.open_workbook('0127_站点地图_03.xlsx')
    sheet = excel.sheet_by_name("Table")
    norws = sheet.nrows
    url_list = []
    for i in range(norws):
        url = sheet.cell(i, 0).value
        url_list.append(url)
    return url_list


findlink = re.compile(r'<a href="(.*?)">')
def get_data(url_list):
    datalist = []
    for url in url_list:
        html = askURL(url)
        # print(html)

        soup = BeautifulSoup(html, "html.parser")
        # print(soup)
        for item in soup.find_all('div', id="app"):
            item = str(item)
            # print(item)
            data = []
            link = re.findall(findlink, item)
            print(link)

def askURL(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 90.0.4430.212Safari / 537.36"
    }
    req = urllib.request.Request(url, headers=head)
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")

    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

if __name__ == '__main__':

    url_list = read_excel()
    get_data(url_list)
