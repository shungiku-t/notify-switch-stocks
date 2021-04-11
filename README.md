# 任天堂スイッチ在庫通知アプリ

## はじめに
マイニンテンドーストアで任天堂スイッチが入荷した際にLINEに通知するアプリ。
品切れ → 入荷 のたびにLINEに通知します。

## 使い方
1. LINE Notifyのトークンを発行します（参考：https://qiita.com/akeome/items/e1e0fecf2e754436afc8
2. .envファイルをプロジェクトルートに作成し、タイムゾーンとLINE Notifyのトークンを記載します
```
TZ=Asia/Tokyo
TOKEN_LINE=<LINE Notifyのトークン>
```
3. docker-compose でコンテナを起動します
