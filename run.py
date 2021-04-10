import requests
from os import getenv
from bs4 import BeautifulSoup


def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = getenv('TOKEN_LINE')
    if not line_notify_token:
        raise Exception('Not found: "TOKEN_LINE"')
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

def has_stocks():
    res = requests.get('https://store-jp.nintendo.com/customize/switch/')
    soup = BeautifulSoup(res.text, 'html.parser')

    state = soup.select_one('div.productDetailSwitchCustomize--detail em').text

    if state == '品切れ':
        return False
    else:
        return True

def main():
    if has_stocks():
        send_line_notify('在庫があるよ！')
    else:
        send_line_notify('在庫がないよ')


if __name__ == "__main__":
    main()
