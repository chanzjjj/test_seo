from atlassian import Confluence
import datetime


def create_confluence(text):
    '''创建confluence页面，把当前时间作为页面title，并返回'''
    time_now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    domain = 'http://wiki.mobvoyage.net'
    confluence = Confluence(
        url=domain,
        username='chenzj',
        password='chenzijia')

    space_key='~陈梓嘉'

    # 参数替换自己的
    page = confluence.create_page(space_key, time_now, text, parent_id= 27825329, type='page', representation='storage', editor='v2')

    path = page['_links']['webui']
    url = domain + path
    print("访问的url: {}".format(url))
    return time_now

if __name__ == '__main__':
    create_confluence("this is a demo")

