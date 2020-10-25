from PhotoHunt import PhotoHunt

url_list = [
    # Todo: 1個未発見
    "https://www.saizeriya.co.jp/entertainment/images/1710/body.png",
    # Perfect!
    "https://www.saizeriya.co.jp/entertainment/images/1801/body.png",
    # Todo: 間違い探し画像の領域推定に失敗してエラー
    # "https://www.saizeriya.co.jp/entertainment/images/1804/body.png",
    # Todo: 2個未発見
    "https://www.saizeriya.co.jp/entertainment/images/1806/body.png",
    # Todo: 間違い探し画像の領域推定に失敗しておりエラーにはなっていないが精度低すぎる
    "https://www.saizeriya.co.jp/entertainment/images/1810/body.png",
    # Todo: 間違い探し画像の領域推定に失敗しておりエラーにはなっていないが精度低すぎる
    "https://www.saizeriya.co.jp/entertainment/images/1812/body.png",
    # Todo: 間違い探し画像の領域推定に失敗しておりエラーにはなっていないが精度低すぎる
    "https://www.saizeriya.co.jp/entertainment/images/1904/body.png",
    # Perfect!
    "https://www.saizeriya.co.jp/entertainment/images/1907/body.png",
    # Perfect!
    "https://www.saizeriya.co.jp/entertainment/images/1910/body.png",
    # Todo: 1個間違いでない箇所を間違いと誤検知
    "https://www.saizeriya.co.jp/entertainment/images/1912/body.png",
    # Todo: 間違い探し画像の領域推定に失敗しておりエラーにはなっていないが精度低すぎる
    "https://www.saizeriya.co.jp/entertainment/images/2003/body.png",
    # Todo: 間違い探し画像の領域推定に失敗しておりエラーにはなっていないが精度低すぎる
    "https://www.saizeriya.co.jp/entertainment/images/2007/body.png",
    # Todo: 間違い探し画像の領域推定に失敗してエラー
    "https://www.saizeriya.co.jp/entertainment/images/2009/body.png"
]

for url in url_list:
    photo_hunt = PhotoHunt(url)
    photo_hunt.execute()
