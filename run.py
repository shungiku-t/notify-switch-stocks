import requests
import pathlib
from os import path, getenv, remove
from bs4 import BeautifulSoup


PATH_LOCKFILE = 'files/lock'

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
    """
    マイ任天堂ストアにてSwitchの在庫があるか否かを真偽値で返す
    """
    res = requests.get('https://store-jp.nintendo.com/customize/switch/')
    soup = BeautifulSoup(res.text, 'html.parser')

    state = soup.select_one('div.productDetailSwitchCustomize--detail em').text

    if state == '品切れ':
        return False
    else:
        return True

def main():
    if has_stocks():
        if not path.exists(PATH_LOCKFILE):
            send_line_notify('在庫があるよ！')
            pathlib.Path(PATH_LOCKFILE).touch()
    else:
        # send_line_notify('在庫がないよ')
        if path.exists(PATH_LOCKFILE): remove(PATH_LOCKFILE)




if __name__ == "__main__":
    main()
