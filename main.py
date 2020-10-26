from PhotoHunt import PhotoHunt

# Todo: 各URLあたり1～2個の未検出、誤検出等の課題はあるが、概ね意図通り動作する状態となった
url_list = [
    "https://www.saizeriya.co.jp/entertainment/images/1710/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1801/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1804/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1806/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1810/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1812/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1904/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1907/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1910/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1912/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/2003/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/2007/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/2009/body.png"
]

for url in url_list:
    photo_hunt = PhotoHunt(url)
    photo_hunt.execute()
