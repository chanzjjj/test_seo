import time
import hmac
import hashlib
import base64
import urllib.parse
import requests
from put2confluence import create_confluence

def send_dingding(url_num, url_question, url_question_num, run_time, url_error, spend_time):
    '''发送钉钉群机器人消息'''

    # 第一步，把timestamp+"\n"+密钥当做签名字符串，使用HmacSHA256算法计算签名，然后进行Base64 encode，最后再把签名参数再进行urlEncode，得到最终的签名（需要使用UTF-8字符集）。
    timestamp = str(round(time.time() * 1000))
    secret = 'SEC1e16498707626642420433db57d5d1298f1c7bdbf4260b2603155da2a910040d'
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    # print(timestamp)
    # print(sign)


    # 第二步，把 timestamp和第一步得到的签名值拼接到URL中。
    Webhook_url = "https://oapi.dingtalk.com/robot/send"
    payload = {
    'access_token': '3f723fea1c07f23d8e46e0d9572b0b234db16e72ddc4bdc58f4a6ae86dbaa932',
    'timestamp': timestamp,
    'sign': sign
    }
    # print(payload)


    # 第三步，发送消息text类型或者link类型、markdown类型、跳转ActionCard类型

    text = "seo检测403结束\n运行的url数量：{}\n有问题的链接：{}\n有问题的链接数量：{}\n运行时间：{}s\n异常的链接：{}\n耗时分布：\n{}".format(url_num, url_question, url_question_num, run_time, url_error, spend_time)
    body = {
    "msgtype": "text",
    "text": {"content": text},
    "at": {"atMobiles": [],"isAtAll": False}
    }
    headers = {'Content-Type': 'application/json; charset=utf-8'}


    r = requests.post(Webhook_url, params=payload, headers=headers, json=body)
    # print(r.url)
    # print(r.text)


def send_dingding_confluence(confluence_text):
    '''发送钉钉-confluence页面'''
    # 第一步，把timestamp+"\n"+密钥当做签名字符串，使用HmacSHA256算法计算签名，然后进行Base64 encode，最后再把签名参数再进行urlEncode，得到最终的签名（需要使用UTF-8字符集）。
    timestamp = str(round(time.time() * 1000))
    secret = 'SEC1e16498707626642420433db57d5d1298f1c7bdbf4260b2603155da2a910040d'
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    # print(timestamp)
    # print(sign)

    # 第二步，把 timestamp和第一步得到的签名值拼接到URL中。
    Webhook_url = "https://oapi.dingtalk.com/robot/send"
    payload = {
        'access_token': '3f723fea1c07f23d8e46e0d9572b0b234db16e72ddc4bdc58f4a6ae86dbaa932',
        'timestamp': timestamp,
        'sign': sign
    }
    # print(payload)

    # 第三步，发送消息text类型或者link类型、markdown类型、跳转ActionCard类型
    now_time = create_confluence(confluence_text)
    url = "http://wiki.mobvoyage.net/display/~%E9%99%88%E6%A2%93%E5%98%89/" + now_time
    text = "seo检测403结束\n具体情况查看：%s" % url
    body = {
        "msgtype": "text",
        "text": {"content": text},
        "at": {"atMobiles": [], "isAtAll": False}
    }
    headers = {'Content-Type': 'application/json; charset=utf-8'}

    r = requests.post(Webhook_url, params=payload, headers=headers, json=body)
    # print(r.url)
    # print(r.text)

if __name__ == '__main__':
    send_dingding("接口名", "接口模块", "接口响应信息", "接口请求时间")