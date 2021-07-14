# Kyamy-Tech
## 確認方法
1. PostgresQLの起動
```
$ brew services start postgresql
```
2. srcフォルダに移動し、実行ファイルの起動
```
$ python3 run.py
```
3. 以下でログイン
```
ID : test
PASSWORD : test
```
4. PostgresQLの停止
```
$ brew services stop postgresql
```

## Kaymy-Techプロジェクト
システム名 "**Z_Generation_Library**"
サイト名   "**福井大学図書館システム**"

ページ構成（表示されるもの）

 - 新規登録画面
  - 学部選択欄
  - 学年選択欄
  - 名前入力欄
  - ユーザID入力欄
  - パスワード入力欄
 - ログイン画面
  - ユーザID入力欄
  - パスワード入力欄
  - ログインボタン
  - 新規登録ボタン
 - TOP画面
  - サイト名
  - 基本機能[TOPボタン、カートボタン、ログアウト]
  - 検索画面への遷移ボタン
  - 学部ごとのランキングクライア
 - 検索窓画面
  - サイト名
  - 基本機能[TOPボタン、カートボタン、ログアウト]
  - 検索ワード入力欄
  - カテゴリ選択欄
  - クライアント名
 - 検索結果画面
  - サイト名
  - 基本機能[TOPボタン、カートボタン、ログアウト]
  - 本のタイトル、著者、詳細ボタン
  - もどるボタン
  - クライアント名
 - 詳細画面
  - サイト名
  - 基本機能[TOPボタン、カートボタン、ログアウト]
  - 本の情報
  - カートに追加ボタン
  - もどるボタン
  - クライアント名
 - カート画面
  - サイト名
  - 基本機能[TOPボタン、カートボタン、ログアウト]
  - カート内の本の情報
  - カート内から本を削除ボタン(個別、全削除)
  - クライアント名